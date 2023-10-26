import { Component, Inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import WorkerSearch from 'src/app/interfaces/worker/worker.search';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormBuilder, FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatCheckboxModule } from '@angular/material/checkbox';

@Component({
  selector: 'app-filter-workers-dialog',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatFormFieldModule, 
    MatInputModule, 
    FormsModule, 
    MatButtonModule,
    MatDividerModule,
    MatCardModule,
    MatSelectModule,
    ReactiveFormsModule,
    MatCheckboxModule,
  ],
  templateUrl: './filter-workers-dialog.component.html',
  styleUrls: ['./filter-workers-dialog.component.css']
})
export class FilterWorkersDialogComponent implements OnInit{

  
  public form!: FormGroup;
  private filterData: WorkerSearch = {};

  allComplete: boolean = false;

  roles: Role = {
    name: 'All Roles',
    completed: false,
    color: 'primary',
    subroles: [
      {name: 'Collections Specialist', completed: false, color: 'primary'},
      {name: 'Collections Supervisor', completed: false, color: 'primary'},
    ],
  };

  constructor(
    public dialogRef: MatDialogRef<FilterWorkersDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: WorkerSearch,
    private fb: FormBuilder,
  ) { }

  ngOnInit(): void {
    this.dialogRef.updateSize('400px', 'auto');

    this.form = this.fb.group({
      name: new FormControl(''),
      contact_info: new FormControl(''),
      roles: new FormControl([]),
    });

    console.log("data: ", this.data);

    this.filterData.name = this.data.name;
    this.filterData.contact_info = this.data.contact_info;
    this.filterData.roles = this.data.roles;

    console.log("filterData: ", this.filterData);

    console.log("name: ", this.data.name)
    console.log("name2: ", this.filterData.name)

    this.form.controls['name'].setValue(this.filterData.name);
    this.form.controls['contact_info'].setValue(this.filterData.contact_info);
    
    this.filterData.roles?.forEach(r => {
      // for each of the roles in the filter data, set the corresponding role in the form to true
      this.roles.subroles?.forEach(role => {
        if (r == role.name){
          role.completed = true;
        }
      });
    });
  
    console.log("form: ", this.form.controls)
  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  onYesClick() {
    this.filterData.name = this.form.get('name')?.value;
    this.filterData.contact_info = this.form.get('contact_info')?.value;
    let roles: string[] = [];
    this.roles.subroles?.forEach(r => {
      if (r.completed){
        roles.push(r.name);
      }
    });
    this.filterData.roles = roles;
    
    this.dialogRef.close(this.filterData);
  }

  updateAllComplete() {
    this.allComplete = this.roles.subroles != null && this.roles.subroles.every(r => r.completed);
  }

  someComplete(): boolean {
    if (this.roles.subroles == null) {
      return false;
    }
    return this.roles.subroles.filter(r => r.completed).length > 0 && !this.allComplete;
  }

  setAll(completed: boolean) {
    this.allComplete = completed;
    if (this.roles.subroles == null) {
      return;
    }
    this.roles.subroles.forEach(r => (r.completed = completed));
  }
}

interface Role {
  name: string;
  completed: boolean;
  color: string;
  subroles?: Role[];
}
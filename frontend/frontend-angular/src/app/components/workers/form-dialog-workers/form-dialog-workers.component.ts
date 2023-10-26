import { Component, Inject, OnDestroy, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MAT_DIALOG_DATA, MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { WorkerDialog } from 'src/app/interfaces/worker/worker.dialog';
import { FormBuilder, FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatDividerModule } from '@angular/material/divider';
import { MatCardModule } from '@angular/material/card';
import { WorkerForm } from 'src/app/interfaces/worker/worker.form';
import { MatSelectModule } from '@angular/material/select';
import { WorkersService } from 'src/app/services/workers.service';
import { Subscription } from 'rxjs/internal/Subscription';

@Component({
  selector: 'app-form-dialog-workers',
  standalone: true,
  imports: [
    CommonModule, 
    MatDialogModule, 
    MatFormFieldModule, 
    MatInputModule, 
    FormsModule, 
    MatButtonModule,
    MatDividerModule,
    MatCardModule,
    MatSelectModule,
    ReactiveFormsModule,
  ],
  templateUrl: './form-dialog-workers.component.html',
  styleUrls: ['./form-dialog-workers.component.css']
})
export class FormDialogWorkersComponent implements OnInit, OnDestroy {

  public form!: FormGroup;
  public formTitle: string = '';
  
  private sendFormSubscription!: Subscription;
  private formSubscription!: Subscription;
  private id: number = -1;

  constructor(
    public dialogRef: MatDialogRef<FormDialogWorkersComponent>,
    @Inject(MAT_DIALOG_DATA) public data: WorkerDialog,
    private workerService: WorkersService,
    private fb: FormBuilder,
  ) { }

  ngOnInit(): void {
    this.dialogRef.updateSize('400px', 'auto');

    this.form = this.fb.group({
      name: new FormControl('', [Validators.required]),
      contact_info: new FormControl('', [Validators.required]),
      role: new FormControl('', [Validators.required]),
    });

    this.formTitle = 'Create a new';

    if (!this.data.id) {
      return;
    }

    this.id = this.data.id;
    
    if (this.data.mode === 'view') {
      this.formTitle = 'View a';
      this.form.disable();
    }else if (this.data.mode === 'edit') {
      this.formTitle = 'Edit a';
    }

    // We get the data of the worker
    this.formSubscription = this.workerService.getWorker(this.data.id)
    .subscribe(
      (response: any) => {
        this.form.controls['name'].setValue(response.name);
        this.form.controls['contact_info'].setValue(response.contact_info);
        this.form.controls['role'].setValue(response.role);
      },
      (error: any) => {
        console.log(error);
      }
    );
  }

  ngOnDestroy(): void {
    if(this.sendFormSubscription)
      this.sendFormSubscription.unsubscribe();
    if(this.formSubscription)
      this.formSubscription.unsubscribe();
  }

  getErrorMessage(): string {
    if (this.form.controls['name'].hasError('required')) {
      return 'You must enter a name';
    }
    if (this.form.controls['contact_info'].hasError('required')) {
      return 'You must enter a contact info';
    }
    if (this.form.controls['role'].hasError('required')) {
      return 'You must select a value';
    }
    return '';
  }

  onNoClick(value: any): void {
    this.dialogRef.close(value);
  }

  async onYesClick(): Promise<void> {
    //send the form data to the backend and if all is good then close the dialog
    if (this.form.invalid) {
      return;
    }

    if (this.data.mode === 'view') {
      this.dialogRef.close();
      return;
    }

    if (this.data.mode === 'edit') {
      this.sendFormSubscription = this.workerService.updateWorker(this.id, {
        name: this.form.controls['name'].value,
        contact_info: this.form.controls['contact_info'].value,
        role: this.form.controls['role'].value,
      })
      .subscribe(
        (response) => {
          console.log("response: ", response)
          this.dialogRef.close(response);
        },
        (error) => {
          console.log("error: ", error)
        }
      )
    } else if (this.data.mode !== 'edit') {

      this.sendFormSubscription = this.workerService.createWorker({
        name: this.form.controls['name'].value,
        contact_info: this.form.controls['contact_info'].value,
        role: this.form.controls['role'].value,
      })
      .subscribe(
        (response) => {
          console.log("response: ", response)
          this.dialogRef.close(response);
        },
        (error) => {
          console.log("error: ", error)
        }
      )
    }
    //

    console.log("yes clicked", this.form.controls);
    //this.dialogRef.close(this.formData);
  }
}

import { Component, Inject, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MAT_DIALOG_DATA, MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { WorkerDialog } from 'src/app/interfaces/worker/worker.dialog';
import { FormControl, FormsModule, Validators } from '@angular/forms';
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
  ],
  templateUrl: './form-dialog-workers.component.html',
  styleUrls: ['./form-dialog-workers.component.css']
})
export class FormDialogWorkersComponent implements OnDestroy {

  formData: WorkerForm = {
    name: '',
    contact_info: '',
    role: ''
  }

  
  name = new FormControl('', [Validators.required]);
  contact_info = new FormControl('', [Validators.required]);
  role = new FormControl('', [Validators.required]);

  private formSubscription!: Subscription;
  
  constructor(
    public dialogRef: MatDialogRef<FormDialogWorkersComponent>,
    @Inject(MAT_DIALOG_DATA) public data: WorkerDialog,
    private workerService: WorkersService,
  ) { }

  ngOnDestroy(): void {
    this.formSubscription.unsubscribe();
  }

  getErrorMessage(): string {
    if (this.name.hasError('required')) {
      return 'You must enter a name';
    }
    if (this.contact_info.hasError('required')) {
      return 'You must enter a contact info';
    }
    if (this.role.hasError('required')) {
      return 'You must select a value';
    }
    return '';
  }

  onNoClick(value: any): void {
    this.dialogRef.close(value);
  }

  async onYesClick(): Promise<void> {
    //send the form data to the backend and if all is good then close the dialog
    this.formSubscription = this.workerService.createWorker(this.formData)
    .subscribe(
      (response) => {
        
        console.log("response: ", response)
        this.dialogRef.close(response);
      },
      (error) => {
        console.log("error: ", error)
      }
    )
    //

        
    console.log("yes clicked", this.formData);
    //this.dialogRef.close(this.formData);
  }
}

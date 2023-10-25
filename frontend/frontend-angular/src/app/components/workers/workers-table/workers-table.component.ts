import { AfterViewInit, Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { MatTableModule } from '@angular/material/table';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { CommonModule, DatePipe, NgIf } from '@angular/common';
import { WorkersService } from 'src/app/services/workers.service';
import { MatSort, MatSortModule } from '@angular/material/sort';
import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { catchError, map, startWith, switchMap } from 'rxjs/operators';
import { Subscription, merge, of as observableOf } from 'rxjs';
import WorkerSearch from 'src/app/interfaces/worker/worker.search';
import { NgIcon } from '@ng-icons/core';
import { MatButtonModule } from '@angular/material/button';
import { FormDialogWorkersComponent } from '../form-dialog-workers/form-dialog-workers.component';

import {MatDialog, MAT_DIALOG_DATA, MatDialogRef, MatDialogModule} from '@angular/material/dialog';
import { DeleteItemDialogComponent } from '../../common/delete-item-dialog/delete-item-dialog.component';

@Component({
  selector: 'app-workers-table',
  standalone: true,
  imports: [
    CommonModule, 
    MatTableModule, 
    MatFormFieldModule, 
    MatButtonModule,
    MatInputModule,
    NgIf,
    MatProgressSpinnerModule,
    MatSortModule,
    MatPaginatorModule,
    DatePipe,
    NgIcon,
    FormDialogWorkersComponent,
    MatDialogModule,
  ],
  templateUrl: './workers-table.component.html',
  styleUrls: ['./workers-table.component.css']
})
export class WorkersTableComponent implements AfterViewInit, OnDestroy {
  displayedColumns: string[] = ['id', 'name', 'contact_info', 'role', 'actions'];
  workers: any[] = [];

  total: number = 0;
  isLoadingResults = true;
  isRateLimitReached = false;
  /*
  add a button that is the advanced search to the table (end of the search bar)
  once clicked, it will open a "dialog" that will have the advanced search options
  that will be a form that will have the following fields:
  name
  contact_info
  role
  and a submit button
  once the submit button is clicked, it will close the dialog and update the table
  with the new search results
  those search results are saved in the args variable*/

  args: WorkerSearch = {};

  page: number = 0;
  pageSize: number = 10;

  private sortSubscription!: Subscription; 
  private sortChangeSubscription!: Subscription; 
  private workerDialogRef!: Subscription; 
  private deleteWorkerSubscription!: Subscription;
  private updateWorkerSubscription!: Subscription;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private workersService: WorkersService, public dialog: MatDialog) { }
  
  ngAfterViewInit() {
    // If the user changes the sort order, reset back to the first page.
    this.sortSubscription = this.sort.sortChange.subscribe(() => (this.paginator.pageIndex = 0));

    this.sortChangeSubscription = merge(this.sort.sortChange, this.paginator.page)
      .pipe(
        startWith({}),
        switchMap(() => {
          this.isLoadingResults = true;
          return this.workersService!.getWorkers(
            this.sort.active,
            this.sort.direction,
            this.paginator.pageIndex,
            this.paginator.pageSize,
            this.args,
          ).pipe(catchError(() => observableOf(null)));
        }),
        map(data => {
          // Flip flag to show that loading has finished.
          this.isLoadingResults = false;
          this.isRateLimitReached = data === null;

          if (data === null) {
            return [];
          }

          // Only refresh the result length if there is new data. In case of rate
          // limit errors, we do not want to reset the paginator to zero, as that
          // would prevent users from re-triggering requests.
          this.total = data.count;
          return data.results;
        }),
      )
      .subscribe(data => (this.workers = data));
  }

  ngOnDestroy(): void {
    if (this.sortSubscription)
      this.sortSubscription.unsubscribe();
    if (this.sortChangeSubscription)
      this.sortChangeSubscription.unsubscribe();
    if (this.workerDialogRef)
      this.workerDialogRef.unsubscribe();
    if (this.deleteWorkerSubscription)
      this.deleteWorkerSubscription.unsubscribe();
    if (this.updateWorkerSubscription)
      this.updateWorkerSubscription.unsubscribe();
  }


  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value.trim().toLowerCase();
    this.args.name = filterValue;

    this.refreshTable();
  }

  filterWorkers() {
    console.log("filter workers clicked")
  }

  addWorker() {
    console.log("add worker clicked")
    const workerDialog = this.dialog.open(FormDialogWorkersComponent, {
      data: {}
    }).afterClosed()
    
    this.workerDialogRef = workerDialog.subscribe(result => {
      console.log('The dialog was closed', result);
      this.refreshTable();
    });
  }

  viewWorker(workerID: number) {
    console.log("view worker clicked with id:", workerID)
    const workerDialog = this.dialog.open(FormDialogWorkersComponent, {
      data: {id: workerID, mode: "view"}
    }).afterClosed()
    
    this.workerDialogRef = workerDialog.subscribe(result => {
      console.log('The dialog was closed', result);
      this.refreshTable();
    });
  }

  editWorker(workerID: number) {
    console.log("edit worker clicked with id:", workerID)
    const workerDialog = this.dialog.open(FormDialogWorkersComponent, {
      data: {id: workerID, mode: "edit"}
    }).afterClosed()
    
    this.workerDialogRef = workerDialog.subscribe(result => {
      console.log('The dialog was closed', result);
      this.refreshTable();
    });
  }

  deleteWorker(workerID: number) {
    console.log("delete worker clicked with id:", workerID)
    const deleteDialog = this.dialog.open(DeleteItemDialogComponent, {
      data: {id: workerID, mode: "edit"}
    }).afterClosed()
    
    this.workerDialogRef = deleteDialog.subscribe(result => {
      console.log('The dialog was closed', result);
      if (result == true) {
        this.deleteWorkerSubscription = this.workersService.deleteWorker(workerID).subscribe(result => {
          console.log('The worker was deleted', result);
          this.refreshTable();
        });
      }
      this.refreshTable();
    });
  }

  refreshTable() {
    this.updateWorkerSubscription = this.workersService.getWorkers(
      this.sort.active,
      this.sort.direction,
      0, // Reset to the first page when applying a filter
      this.paginator.pageSize,
      this.args
    ).pipe(
      catchError(() => observableOf(null))
    ).subscribe(data => {
      if (data === null) {
        // Handle error if necessary
      } else {
        this.total = data.count;
        this.workers = data.results;
      }
    });

    if (this.paginator) {
      this.paginator.firstPage();
    }
  }
}

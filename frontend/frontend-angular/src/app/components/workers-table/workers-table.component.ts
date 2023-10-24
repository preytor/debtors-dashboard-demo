import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { MatTableModule } from '@angular/material/table';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { CommonModule, DatePipe, NgIf } from '@angular/common';
import { WorkerResults } from 'src/app/interfaces/worker.results';
import { WorkersService } from 'src/app/services/workers.service';
import { MatSort, MatSortModule } from '@angular/material/sort';
import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { catchError, map, startWith, switchMap } from 'rxjs/operators';
import { merge, of as observableOf } from 'rxjs';
import WorkerSearch from 'src/app/interfaces/worker.search';

@Component({
  selector: 'app-workers-table',
  standalone: true,
  imports: [
    CommonModule, 
    MatTableModule, 
    MatFormFieldModule, 
    MatInputModule,
    NgIf,
    MatProgressSpinnerModule,
    MatSortModule,
    MatPaginatorModule,
    DatePipe,
  ],
  templateUrl: './workers-table.component.html',
  styleUrls: ['./workers-table.component.css']
})
export class WorkersTableComponent implements AfterViewInit {
  displayedColumns: string[] = ['id', 'name', 'contact_info', 'role'];
  workers: any[] = [];

  total: number = 0;
  isLoadingResults = true;
  isRateLimitReached = false;

  args: WorkerSearch = {};

  page: number = 0;
  pageSize: number = 10;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private workersService: WorkersService) { }


  ngAfterViewInit() {
    // If the user changes the sort order, reset back to the first page.
    this.sort.sortChange.subscribe(() => (this.paginator.pageIndex = 0));

    merge(this.sort.sortChange, this.paginator.page)
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
          console.log("data.results", data.results)
          return data.results;
        }),
      )
      .subscribe(data => (this.workers = data));
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value.trim().toLowerCase();
    console.log("filter value is ", filterValue)
    this.args.name = filterValue;

    this.workersService.getWorkers(
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

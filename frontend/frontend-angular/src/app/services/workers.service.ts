import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { WorkerResults } from '../interfaces/worker.results';
import { SortDirection } from '@angular/material/sort';
import WorkerSearch from '../interfaces/worker.search';

@Injectable({
  providedIn: 'root'
})
export class WorkersService {

  constructor(private http: HttpClient) { }


  getWorkers(sort: string = "", order: SortDirection = 'asc', page: number = 1, perPage: number = 10, args: WorkerSearch = {}): Observable<WorkerResults> {
    let final_args = "";
    if (sort != "") {
      let orderDirection = order.toString() == "desc" ? "-" : "";
      final_args += `&ordering=${orderDirection}${sort}`;
    }
    if (args.name) {
      final_args += `&name=${args.name}`;
    }
    if (args.contact_info) {
      final_args += `&contact_info=${args.contact_info}`;
    }
    if (args.role) {
      final_args += `&role=${args.role}`;
    }
    console.log(`${environment.backend_url}/api/workers?page=${page+1}&page_size=${perPage}${final_args}`)
    const response = this.http.get<WorkerResults>(`${environment.backend_url}/api/workers?page=${page+1}&page_size=${perPage}${final_args}`);
    return response;
  }
}

import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { WorkerResults } from '../interfaces/worker/worker.results';
import { SortDirection } from '@angular/material/sort';
import WorkerSearch from '../interfaces/worker/worker.search';
import { WorkerForm } from '../interfaces/worker/worker.form';

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
    if (args.roles) {
      for (let role of args.roles) {
        final_args += `&roles=${role}`;
      }
    }
    
    const response = this.http.get<WorkerResults>(`${environment.backend_url}/api/workers?page=${page+1}&page_size=${perPage}${final_args}`);
    return response;
  }

  createWorker(workerData: WorkerForm): Observable<any> {
    let workerFormData = new FormData();
    workerFormData.append('name', workerData.name);
    workerFormData.append('contact_info', workerData.contact_info);
    workerFormData.append('role', workerData.role);

    return this.http.post(`${environment.backend_url}/api/worker`, workerFormData);
  }

  deleteWorker(workerId: number): Observable<any> {
    return this.http.delete(`${environment.backend_url}/api/worker/${workerId}`);
  }
}

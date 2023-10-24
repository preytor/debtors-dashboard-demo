import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WorkersTableComponent } from './components/workers-table/workers-table.component';
import { CasesComponent } from './components/cases/cases.component';
import { DebtorsComponent } from './components/debtors/debtors.component';

const routes: Routes = [
  {
    path:'workers', component: WorkersTableComponent,
  },
  {
    path:'debtors', component: DebtorsComponent,
  },
  {
    path:'cases', component: CasesComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

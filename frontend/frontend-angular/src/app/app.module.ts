import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/layout/header/header.component';
import { SidebarComponent } from './components/layout/sidebar/sidebar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule } from '@angular/material/toolbar';
import { HeaderIconProfileComponent } from './components/layout/header-icon-profile/header-icon-profile.component';
import { NgIconsModule } from '@ng-icons/core';
import { 
  bootstrapDoorOpenFill, 
  bootstrapEyeFill, 
  bootstrapFilePersonFill, 
  bootstrapFolderFill, 
  bootstrapGearFill, 
  bootstrapList, 
  bootstrapPencilSquare, 
  bootstrapPersonFill, 
  bootstrapPersonVcardFill,
  bootstrapTrash3Fill
} from '@ng-icons/bootstrap-icons';
import { matFilterAltSharp } from '@ng-icons/material-icons/sharp';
import { DebtorsComponent } from './components/debtors/debtors.component';
import { CasesComponent } from './components/cases/cases.component';
import { HttpClientModule } from '@angular/common/http';
import { FormDialogWorkersComponent } from './components/workers/form-dialog-workers/form-dialog-workers.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    SidebarComponent,
    HeaderIconProfileComponent,
    DebtorsComponent,
    CasesComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    NgIconsModule.withIcons({ 
      bootstrapPersonFill,
      bootstrapGearFill,
      bootstrapDoorOpenFill,
      bootstrapList,
      bootstrapPersonVcardFill,
      bootstrapFilePersonFill,
      bootstrapFolderFill,
      bootstrapEyeFill,
      bootstrapPencilSquare,
      bootstrapTrash3Fill,
      matFilterAltSharp,
    }),
    MatToolbarModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

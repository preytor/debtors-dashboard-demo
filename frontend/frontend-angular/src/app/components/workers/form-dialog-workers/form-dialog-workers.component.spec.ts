import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormDialogWorkersComponent } from './form-dialog-workers.component';

describe('FormDialogWorkersComponent', () => {
  let component: FormDialogWorkersComponent;
  let fixture: ComponentFixture<FormDialogWorkersComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [FormDialogWorkersComponent]
    });
    fixture = TestBed.createComponent(FormDialogWorkersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

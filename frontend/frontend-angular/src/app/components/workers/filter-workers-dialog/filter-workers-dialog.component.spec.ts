import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FilterWorkersDialogComponent } from './filter-workers-dialog.component';

describe('FilterWorkersDialogComponent', () => {
  let component: FilterWorkersDialogComponent;
  let fixture: ComponentFixture<FilterWorkersDialogComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [FilterWorkersDialogComponent]
    });
    fixture = TestBed.createComponent(FilterWorkersDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

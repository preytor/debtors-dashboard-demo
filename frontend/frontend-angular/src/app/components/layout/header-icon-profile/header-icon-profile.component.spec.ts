import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderIconProfileComponent } from './header-icon-profile.component';

describe('HeaderIconProfileComponent', () => {
  let component: HeaderIconProfileComponent;
  let fixture: ComponentFixture<HeaderIconProfileComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [HeaderIconProfileComponent]
    });
    fixture = TestBed.createComponent(HeaderIconProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

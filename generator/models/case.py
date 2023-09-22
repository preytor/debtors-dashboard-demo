import random
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Float, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase

from models.worker import Worker
from models.debtor import Debtor

from enums.case_status_enum import CaseStatusEnum
from enums.payment_frequency_enum import PaymentFrequencyEnum

class Base(DeclarativeBase):
    pass

class Case(Base):
    __tablename__ = "case"

    id = Column(Integer, primary_key=True, autoincrement=True)
    debtor_id = Column(Integer, ForeignKey(Debtor.id), nullable=False)
    assigned_worker_id = Column(Integer, ForeignKey(Worker.id), nullable=False)
    borrowed_amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    amortization_period = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    # Define the choices for the case_status field as an ENUM
    case_status_enum = CaseStatusEnum
    case_status = Column(String, default=case_status_enum.OPEN.value)

    # Define the choices for the case payment_frequency field as an ENUM
    payment_frequency_enum = PaymentFrequencyEnum
    payment_frequency = Column(String, default=payment_frequency_enum.WEEKLY.value)

    def generate_data(self):
        self.borrowed_amount = random.randint(1000, 100000)
        self.interest_rate = random.uniform(0.01, 0.10)
        self.amortization_period = random.randint(1, 25)
        self.created_at = datetime(random.randint(2000, 2023), random.randint(1, 12), random.randint(1, 28))
        self.case_status = random.choice(list(self.case_status_enum)).value
        self.payment_frequency = random.choice(list(self.payment_frequency_enum)).value
    
    '''
    def generate_random_payments(self, PAYMENTS_PERCENTAGES, PAYMENTS_FAILED_PERCENTAGE, session) -> int:
        """ We generate the amount of payments based on the amortization period and the status of the case """
        # We define the payments_to_insert
        payments_to_insert = []
        
        years = self.amortization_period
        # Calculate the monthly interest rate
        monthly_interest_rate = self.interest_rate / 12
        # Calculate the monthly payment using the formula
        monthly_payment_cuota = (
            self.borrowed_amount
            * monthly_interest_rate
            * (1 + monthly_interest_rate) ** (years * 12)
        ) / ((1 + monthly_interest_rate) ** (years * 12) - 1)

        # We define the starting month of the payments
        month_cuota_date = datetime(self.created_at.year, self.created_at.month, self.created_at.day)

        # If the status is closed we make all of the payments
        if self.case_status == self.case_status_enum.CLOSED.value:
            for _ in range(years):
                # We increment the month by one in the month_cuota_date
                month_cuota_date = month_cuota_date + timedelta(days=30)
                # We set the day at 1 so is the first of the month
                month_cuota_date = month_cuota_date.replace(day=1)

                # We generate the payment
                payments_manager = PaymentsManager(case_id=self.id)
                payments = payments_manager.generate_payments_per_frequency(self.payment_frequency, monthly_payment_cuota, month_cuota_date)
                
                payments_to_insert.extend(payments)
        elif self.case_status == self.case_status_enum.OPEN.value:
            # We generate the payments that are not paid
            # We calculate the percentage of payments that are paid based on the PAYMENTS_PERCENTAGES
            years_paid = random.randint(int(years * PAYMENTS_PERCENTAGES[0] / 100), int(years * PAYMENTS_PERCENTAGES[1] / 100))
            for _ in range(years_paid):
                # We increment the month by one in the month_cuota_date
                month_cuota_date = month_cuota_date + timedelta(days=30)
                # We set the day at 1 so is the first of the month
                month_cuota_date = month_cuota_date.replace(day=1)

                # We generate the payment
                payments_manager = PaymentsManager(case_id=self.id)
                payments = payments_manager.generate_payments_per_frequency(self.payment_frequency, monthly_payment_cuota, month_cuota_date)
                
                payments_to_insert.extend(payments)
            # we add a small % of a failed payment
            percentage = random.randint(0, 100)
            if percentage <= PAYMENTS_FAILED_PERCENTAGE:
                # We get the last payment to keep track of the date
                last_payment = payments_to_insert[-1]
                payments_manager = PaymentsManager(case_id=self.id)
                payment = payments_manager.generate_missed_payment(last_payment)
                payments_to_insert.append(payment)
            
        # We bulk insert the data in payments_to_insert
        session.bulk_save_objects(payments_to_insert)
        session.flush()
        return len(payments_to_insert)
    '''
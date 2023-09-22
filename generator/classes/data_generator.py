import random

from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker, scoped_session

from models.case import Case
from models.debtor import Debtor
from models.worker import Worker
from models.payments_manager import PaymentsManager

class DataGenerator:

    def __init__(self, 
                first_names, 
                last_names,
                DEBTORS_PER_WORKER, 
                CASES_PER_DEBTOR, 
                PAYMENTS_PERCENTAGES, 
                PAYMENTS_FAILED_PERCENTAGE
            ) -> None:
        self.first_names = first_names
        self.last_names = last_names
        self.DEBTORS_PER_WORKER = DEBTORS_PER_WORKER
        self.CASES_PER_DEBTOR = CASES_PER_DEBTOR
        self.PAYMENTS_PERCENTAGES = PAYMENTS_PERCENTAGES
        self.PAYMENTS_FAILED_PERCENTAGE = PAYMENTS_FAILED_PERCENTAGE


    def process_generated_data(self, session_factory: sessionmaker) -> tuple:
        """
            We process all of the data to insert
            First we create the workers of the company
            Then we insert the debtors managed by each of those workers
            Then we insert the cases managed for each of the debtors
            Then we insert the payments for each of the cases
        """
        workers_to_insert_count = 0
        debtors_to_insert_count = 0
        cases_to_insert_count = 0
        payments_to_insert_count = 0

        Session = scoped_session(session_factory)
        with Session() as session:
            # We create and insert the worker
            worker = Worker()
            worker.generate_data(self.first_names, self.last_names)
            workers_to_insert_count += 1
            session.add(worker)
            session.commit()

            # We create and insert the debtors for the worker
            if type(self.DEBTORS_PER_WORKER) == int:
                loop_condition = range(self.DEBTORS_PER_WORKER)
            elif type(self.DEBTORS_PER_WORKER) == list:
                loop_condition = range(random.randint(self.DEBTORS_PER_WORKER[0], self.DEBTORS_PER_WORKER[1]))

            for _ in loop_condition:
                debtor = Debtor()
                debtor.generate_data(self.first_names, self.last_names)
                debtors_to_insert_count += 1
                
                session.add(debtor)
                session.commit()

                # We create and insert the cases for the debtor
                if type(self.CASES_PER_DEBTOR) == int:
                    loop_condition = range(self.CASES_PER_DEBTOR)
                elif type(self.CASES_PER_DEBTOR) == list:
                    loop_condition = range(random.randint(self.CASES_PER_DEBTOR[0], self.CASES_PER_DEBTOR[1]))

                for _ in loop_condition:
                    case = Case()
                    case.generate_data()
                    case.debtor_id = debtor.id
                    case.assigned_worker_id = worker.id
                    cases_to_insert_count += 1

                    session.add(case)
                    session.commit()

                    payments_to_insert_count += self.generate_random_payments(case, self.PAYMENTS_PERCENTAGES, self.PAYMENTS_FAILED_PERCENTAGE, session)

        return tuple((workers_to_insert_count, debtors_to_insert_count, cases_to_insert_count, payments_to_insert_count))
    
    def generate_random_payments(self, case, PAYMENTS_PERCENTAGES, PAYMENTS_FAILED_PERCENTAGE, session) -> int:
        """ We generate the amount of payments based on the amortization period and the status of the case """
        # We define the payments_to_insert
        payments_to_insert = []
        
        years = case.amortization_period
        # Calculate the monthly interest rate
        monthly_interest_rate = case.interest_rate / 12
        # Calculate the monthly payment using the formula
        monthly_payment_cuota = (
            case.borrowed_amount
            * monthly_interest_rate
            * (1 + monthly_interest_rate) ** (years * 12)
        ) / ((1 + monthly_interest_rate) ** (years * 12) - 1)

        # We define the starting month of the payments
        month_cuota_date = datetime(case.created_at.year, case.created_at.month, case.created_at.day)

        # If the status is closed we make all of the payments
        if case.case_status == case.case_status_enum.CLOSED.value:
            for _ in range(years):
                # We increment the month by one in the month_cuota_date
                month_cuota_date = month_cuota_date + timedelta(days=30)
                # We set the day at 1 so is the first of the month
                month_cuota_date = month_cuota_date.replace(day=1)

                # We generate the payment
                payments_manager = PaymentsManager(case_id=case.id)
                payments = payments_manager.generate_payments_per_frequency(case.payment_frequency, monthly_payment_cuota, month_cuota_date)
                
                payments_to_insert.extend(payments)
        elif case.case_status == case.case_status_enum.OPEN.value:
            # We generate the payments that are not paid
            # We calculate the percentage of payments that are paid based on the PAYMENTS_PERCENTAGES
            years_paid = random.randint(int(years * PAYMENTS_PERCENTAGES[0] / 100)+1, int(years * PAYMENTS_PERCENTAGES[1] / 100)+1)
            for _ in range(years_paid):
                # We increment the month by one in the month_cuota_date
                month_cuota_date = month_cuota_date + timedelta(days=30)
                # We set the day at 1 so is the first of the month
                month_cuota_date = month_cuota_date.replace(day=1)

                # We generate the payment
                payments_manager = PaymentsManager(case_id=case.id)
                payments = payments_manager.generate_payments_per_frequency(case.payment_frequency, monthly_payment_cuota, month_cuota_date)
                
                payments_to_insert.extend(payments)
            # we add a small % of a failed payment
            percentage = random.randint(0, 100)
            if percentage <= PAYMENTS_FAILED_PERCENTAGE:
                # We get the last payment to keep track of the date
                last_payment = payments_to_insert[-1]
                payments_manager = PaymentsManager(case_id=case.id)
                payment = payments_manager.generate_missed_payment(last_payment)
                payments_to_insert.append(payment)
            
        # We bulk insert the data in payments_to_insert
        session.bulk_save_objects(payments_to_insert)
        session.flush()
        return len(payments_to_insert)
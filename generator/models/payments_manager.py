import random

from datetime import timedelta

from enums.payment_frequency_enum import PaymentFrequencyEnum
from enums.payment_status_enum import PaymentStatusEnum

from models.payment import Payment

class PaymentsManager:
    def __init__(self, case_id):
        self.case_id = case_id

    def generate_payments_per_frequency(self, payment_frequency, monthly_payment_cuota, month_cuota_date) -> list[Payment]:
        """ We generate a list of payments of this year based on the frequency of the payment """
        payments: list[Payment] = []
        if payment_frequency == PaymentFrequencyEnum.WEEKLY.value:
            payments.extend(self.generate_weekly_payments(monthly_payment_cuota, month_cuota_date))
        elif payment_frequency == PaymentFrequencyEnum.BI_WEEKLY.value:
            payments.extend(self.generate_biweekly_payments(monthly_payment_cuota, month_cuota_date))
        elif payment_frequency == PaymentFrequencyEnum.MONTHLY.value:
            payments.extend(self.generate_monthly_payments(monthly_payment_cuota, month_cuota_date))

        return payments
        
    def generate_weekly_payments(self, monthly_payment_cuota, month_cuota_date) -> list[Payment]:
        payments = []
        for _ in range(4):
            status = random.choice([PaymentStatusEnum.ON_TIME.value, PaymentStatusEnum.LATE.value])
            payment = Payment(
                case_id = self.case_id,
                payment_date=month_cuota_date if status == PaymentStatusEnum.ON_TIME.value else month_cuota_date + timedelta(days=random.randint(1, 6)),
                payment_amount=monthly_payment_cuota/4,
                payment_status=status,
            )
            payments.append(payment)
            # We add 15 days to the date of the payment for the next payment
            month_cuota_date += timedelta(days=7)
        return payments

    def generate_biweekly_payments(self, monthly_payment_cuota, month_cuota_date) -> list[Payment]:
        payments = []
        for _ in range(2):
            status = random.choice([PaymentStatusEnum.ON_TIME.value, PaymentStatusEnum.LATE.value])
            payment = Payment(
                case_id = self.case_id,
                payment_date=month_cuota_date if status == PaymentStatusEnum.ON_TIME.value else month_cuota_date + timedelta(days=random.randint(1, 6)),
                payment_amount=monthly_payment_cuota/2,
                payment_status=status,
            )
            payments.append(payment)
            # We add 15 days to the date of the payment for the next payment
            month_cuota_date += timedelta(days=15)
        return payments

    def generate_monthly_payments(self, monthly_payment_cuota, month_cuota_date) -> list[Payment]:
        status = random.choice([PaymentStatusEnum.ON_TIME.value, PaymentStatusEnum.LATE.value])

        payment = Payment(
            case_id = self.case_id,
            payment_date=month_cuota_date if status == PaymentStatusEnum.ON_TIME.value else month_cuota_date + timedelta(days=random.randint(1, 6)),
            payment_amount=monthly_payment_cuota,
            payment_status=status,
        )
        return [payment]
    
    def generate_missed_payment(self, last_payment):
        payment = Payment(
            case_id = self.case_id,
            payment_date=(last_payment.payment_date + timedelta(days=30)).replace(day=28),
            payment_amount=last_payment.payment_amount,
            payment_status=PaymentStatusEnum.MISSED.value,
        )
        return payment
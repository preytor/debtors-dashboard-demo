from django.test import TestCase
from rest_framework.test import APIRequestFactory

from datetime import date

from .models import Payment
from debtors.models import Debtor
from .forms import PaymentForm

# Create your tests here.
class PaymentTestCase(TestCase):
    def setUp(self):
        debtor = Debtor.objects.create(
            name='test',
            contact_info='test',
            initial_debt=1000,
            legal_status='Active',
        )
        Payment.objects.create(
            debtor=debtor,
            payment_date=date(2021, 1, 1),
            payment_amount=100,
            payment_status="On time",
        )
        Payment.objects.create(
            debtor=debtor,
            payment_date=date(2021, 2, 10),
            payment_amount=100,
            payment_status="Late",
        )

    def test_created_payment(self):
        payment1 = Payment.objects.get(payment_date=date(2021, 1, 1))
        payment2 = Payment.objects.get(payment_date=date(2021, 2, 10))
        self.assertEqual(payment1.payment_date, date(2021, 1, 1))
        self.assertEqual(payment2.payment_date, date(2021, 2, 10))

    def test_update_payment(self):
        payment1 = Payment.objects.get(payment_date=date(2021, 2, 10))
        payment1.payment_status = "Missed"
        payment1.save()
        self.assertEqual(payment1.payment_status, "Missed")
        self.assertNotEqual(payment1.payment_status, "Late")

    def test_delete_payment(self):
        payment2 = Payment.objects.get(payment_date=date(2021, 2, 10))
        payment2.delete()
        self.assertEqual(Payment.objects.count(), 1)
        self.assertNotEqual(Payment.objects.count(), 2)

class PaymentFormTestCase(TestCase):

    def test_is_invalid(self):
        form = PaymentForm(data={
            'debtor': '',
            'payment_date': '',
            'payment_amount': '',
            'payment_status': '',
        })
        self.assertFalse(form.is_valid())

    def test_is_valid(self):
        debtor = Debtor.objects.create(
            name='test',
            contact_info='test',
            initial_debt=1000,
            legal_status='Active',
        )
        form = PaymentForm(data={
            'debtor': Debtor.objects.get(id=debtor.id).id,
            'payment_date': date(2021, 1, 1),
            'payment_amount': 100,
            'payment_status': 'On time',
        })
        self.assertTrue(form.is_valid())

class PaymentApiTestCase(TestCase):

    def setUp(self):
        self.debtor = Debtor.objects.create(
            name='test',
            contact_info='test',
            initial_debt=1000,
            legal_status='Active',
        )
        self.payment = Payment.objects.create(
            debtor=self.debtor,
            payment_date=date(2021, 1, 1),
            payment_amount=100,
            payment_status="On time",
        )

    # Get all payments for a debtor
    def test_get_all_payments_from_debtor(self):
        response = self.client.get(f'/api/payments/{self.debtor.id}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_payments_from_debtor_with_params(self):
        response = self.client.get(f'/api/payments/{self.debtor.id}?payment_status=On%20time')
        self.assertEqual(response.status_code, 200)

    def test_payment_found(self):
        response = self.client.get(f'/api/payments/{self.debtor.id}')
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_payment_not_found(self):
        response = self.client.get(f'/api/payments/{self.debtor.id}?payment_status=Missed')
        self.assertEqual(len(response.data['results']), 0)

    # Create a payment
    def test_post_payment(self):
        response = self.client.post(f'/api/payment', {
            'debtor': self.debtor.id,
            'payment_date': date(2021, 2, 1),
            'payment_amount': 100,
            'payment_status': 'On time',
        })
        self.assertEqual(response.status_code, 201)
        self.assertDictContainsSubset(response.data, {
            'debtor': f'{self.debtor.id}',
            'payment_date': '2021-02-01',
            'payment_amount': '100',
            'payment_status': 'On time',
        })

    # Get payment by id
    def test_get_payment(self):
        response = self.client.get(f'/api/payment/{self.payment.id}')
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(response.data, {
            'id': self.payment.id,
            'debtor': self.debtor.id,
            'payment_date': '2021-01-01',
            'payment_amount': '100.00',
            'payment_status': 'On time',
        })

    # Update payment by id
    def test_put_payment(self):
        response = self.client.put(path=f'/api/payment/{self.payment.id}', data={
            'debtor': self.debtor.id,
            'payment_date': date(2021, 1, 1),
            'payment_amount': 100,
            'payment_status': 'Missed',
        }, content_type='application/json', data_type='json')
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(response.data, {
            'debtor': self.debtor.id,
            'payment_date': '2021-01-01',
            'payment_amount': 100,
            'payment_status': 'Missed',
        })

    # Delete payment by id
    def test_delete_payment(self):
        response = self.client.delete(f'/api/payment/{self.payment.id}')
        self.assertEqual(response.status_code, 200)
        
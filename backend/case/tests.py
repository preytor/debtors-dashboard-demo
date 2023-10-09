from unittest import mock
from django.test import TestCase
from rest_framework.test import APIRequestFactory

import pytz
import datetime

from .models import Case
from debtors.models import Debtor
from worker.models import Worker
from .forms import CaseForm

# Create your tests here.
class CaseTestCase(TestCase):
    def setUp(self):
        debtor = Debtor.objects.create(
            name='test',
            contact_info='test',
            legal_status='Active',
        )
        worker = Worker.objects.create(
            name='test',
            contact_info='test',
            role='test',
        )
        Case.objects.create(
            debtor=debtor,
            assigned_worker=worker,
            case_status="Open",
        )
        Case.objects.create(
            debtor=debtor,
            assigned_worker=worker,
            case_status="In progress",
        )

    def test_created_case(self):
        case1 = Case.objects.get(case_status="Open")
        case2 = Case.objects.get(case_status="In progress")
        self.assertEqual(case1.case_status, "Open")
        self.assertEqual(case2.case_status, "In progress")

    def test_update_case(self):
        case1 = Case.objects.get(case_status="Open")
        case1.case_status = "Closed"
        case1.save()
        self.assertEqual(case1.case_status, "Closed")
        self.assertNotEqual(case1.case_status, "Open")

    def test_delete_case(self):
        case2 = Case.objects.get(case_status="In progress")
        case2.delete()
        self.assertEqual(Case.objects.count(), 1)
        self.assertNotEqual(Case.objects.count(), 2)

class CaseFormTestCase(TestCase):

    def test_is_invalid(self):
        form = CaseForm(data={
            'debtor': '',
            'assigned_worker': '',
            'case_status': '',
        })
        self.assertFalse(form.is_valid())

    def test_is_valid(self):
        debtor = Debtor.objects.create(
            name='test',
            contact_info='test',
            legal_status='Active',
        )
        worker = Worker.objects.create(
            name='test',
            contact_info='test',
            role='test',
        )
        form = CaseForm(data={
            'debtor': Debtor.objects.get(name=debtor.name),
            'assigned_worker': Worker.objects.get(name=worker.name),
            'case_status': 'Open',
        })
        self.assertTrue(form.is_valid())

class CaseApiTestCase(TestCase):
    def setUp(self):
        self.debtor = Debtor.objects.create(
            name='test',
            contact_info='test',
            legal_status='Active',
        )
        self.worker = Worker.objects.create(
            name='test',
            contact_info='test',
            role='test',
        )
        self.case = Case.objects.create(
            debtor=self.debtor,
            assigned_worker=self.worker,
            case_status="Open",
            borrowed_amount=1000,
            payment_frequency=None,
            interest_rate=1,
            amortization_period=1,
            created_at="2023-10-09T04:30:00Z"
        )

    # Get all cases from a debtor
    def test_get_all_cases_from_debtor(self):
        response = self.client.get(f'/api/cases?debtor={self.debtor.id}')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data['results']), 1)

    # Get all cases from a worker
    def test_get_all_cases_from_worker(self):
        response = self.client.get(f'/api/cases?assigned_worker={self.worker.id}')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data['results']), 1)

    # Get all cases from a worker and a debtor
    def test_get_all_cases_from_worker_and_debtor(self):
        response = self.client.get(f'/api/cases?assigned_worker={self.worker.id}&debtor={self.debtor.id}')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_case_not_found(self):
        response = self.client.get(f'/api/cases?assigned_worker={self.worker.id + 1}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 0)

    # Create a case
    def test_post_case(self):
        response = self.client.post('/api/case', {
            'debtor': self.debtor.id,
            'assigned_worker': self.worker.id,
            'case_status': 'Open',
        })
        self.assertEqual(response.status_code, 201)
        self.assertDictContainsSubset(response.data, {
            'id': self.case.id,
            'debtor': f'{self.debtor.id}',
            'assigned_worker': f'{self.worker.id}',
            'case_status': 'Open',
        })

    # Get case by id
    def test_get_case(self):
        response = self.client.get(f'/api/case/{self.case.id}')
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(response.data, {
            'id': self.case.id,
            'debtor': self.debtor.id,
            'assigned_worker': self.worker.id,
            'case_status': 'Open',
            'borrowed_amount': '1000.00',
            'payment_frequency': None,
            'interest_rate': '1.00',
            'amortization_period': 1,
            'created_at': self.case.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        })

    # Update case
    @mock.patch('django.utils.timezone.now')
    def test_put_case(self, mock_now):
        mock_now.return_value = datetime.datetime(2023, 10, 9, 4, 30, tzinfo=pytz.UTC).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        response = self.client.put(f'/api/case/{self.case.id}', data={
            'debtor': self.debtor.id,
            'assigned_worker': self.worker.id,
            'case_status': 'Closed',
            'borrowed_amount': 1000,
            'payment_frequency': None,
            'interest_rate': 1,
            'amortization_period': 1
        }, content_type='application/json', data_type='json')
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(response.data, {
            'id': self.case.id,
            'debtor': self.debtor.id,
            'assigned_worker': self.worker.id,
            'case_status': 'Closed',
            'borrowed_amount': '1000.00',
            'payment_frequency': None,
            'interest_rate': '1.00',
            'amortization_period': 1,
            'created_at': response.data['created_at'],
        })

    # Delete case
    def test_delete_case(self):
        response = self.client.delete(f'/api/case/{self.case.id}')
        self.assertEqual(response.status_code, 200)

from django.test import TestCase

from .models import Debtor
from .forms import DebtorForm

# Create your tests here.
class DebtorTestCase(TestCase):
    def setUp(self):
        Debtor.objects.create(
            name='test',
            contact_info='test',
            legal_status='Active',
        )
        Debtor.objects.create(
            name='test2',
            contact_info='test',
            legal_status='Active',
        )

    def test_created_debtor(self):
        debtor1 = Debtor.objects.get(name='test')
        debtor2 = Debtor.objects.get(name='test2')
        self.assertEqual(debtor1.name, 'test')
        self.assertEqual(debtor2.name, 'test2')

    def test_update_debtor(self):
        debtor1 = Debtor.objects.get(name='test')
        debtor1.name = 'test3'
        debtor1.save()
        self.assertEqual(debtor1.name, 'test3')
        self.assertNotEqual(debtor1.name, 'test')

    def test_delete_debtor(self):
        debtor2 = Debtor.objects.get(name='test2')
        debtor2.delete()
        self.assertEqual(Debtor.objects.count(), 1)
        self.assertNotEqual(Debtor.objects.count(), 2)

class DebtorFormTestCase(TestCase):

    def test_is_invalid(self):
        form = DebtorForm(data={
            'name': '',
            'contact_info': '',
            'legal_status': '',
        })
        self.assertFalse(form.is_valid())

    def test_is_valid(self):
        form = DebtorForm(data={
            'name': 'test',
            'contact_info': 'test',
            'legal_status': 'Active',
        })
        self.assertTrue(form.is_valid())

class DebtorApiTestCase(TestCase):

    def setUp(self):
        self.debtor = Debtor.objects.create(
            name='test',
            contact_info='test',
            legal_status='Active',
        )
    
    # get all debtors
    def test_get_all_debtors(self):
        response = self.client.get('/api/debtors')
        self.assertEqual(response.status_code, 200)

    def test_get_all_debtors_with_params(self):
        response = self.client.get('/api/debtors?name=test')
        self.assertEqual(response.status_code, 200)

    # Create a debtor
    def test_post_worker(self):
        response = self.client.post('/api/debtor', {
            'name': 'test',
            'contact_info': 'test',
            'legal_status': 'Active',
        })
        self.assertEqual(response.status_code, 201)
        self.assertDictContainsSubset(response.data, {
            'name': 'test',
            'contact_info': 'test',
            'legal_status': 'Active',
        })

    # Get a debtor by id
    def test_get_debtor(self):
        id = self.debtor.id
        response = self.client.get(f'/api/debtor/{id}')
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(response.data, {
            'id': id,
            'name': 'test',
            'contact_info': 'test',
            'legal_status': 'Active',
        })

    # Update a debtor by id
    def test_put_debtor(self):
        id = self.debtor.id
        response = self.client.put(f'/api/debtor/{id}', data={
            'name': 'test2',
            'contact_info': 'test',
            'legal_status': 'Active',
        }, content_type='application/json', data_type='json')
        print("response", response.data)
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(response.data, {
            'id': id,
            'name': 'test2',
            'contact_info': 'test',
            'legal_status': 'Active',
        })

    # Delete a debtor by id
    def test_delete_debtor(self):
        id = self.debtor.id
        response = self.client.delete(f'/api/debtor/{id}')
        self.assertEqual(response.status_code, 200)

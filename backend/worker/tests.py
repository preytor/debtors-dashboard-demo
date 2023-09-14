from django.test import TestCase
from rest_framework.test import APIRequestFactory

from .models import Worker
from .forms import WorkerForm


# Create your tests here.
class WorkerTestCase(TestCase):
    def setUp(self):
        Worker.objects.create(
            name='test',
            contact_info='test',
            role='test',
        )
        Worker.objects.create(
            name='test2',
            contact_info='test2',
            role='test2',
        )

    def test_created_worker(self):
        worker1 = Worker.objects.get(name='test')
        worker2 = Worker.objects.get(name='test2')
        self.assertEqual(worker1.name, 'test')
        self.assertEqual(worker2.name, 'test2')

    def test_update_worker(self):
        worker1 = Worker.objects.get(name='test')
        worker1.name = 'test3'
        worker1.save()
        self.assertEqual(worker1.name, 'test3')
        self.assertNotEqual(worker1.name, 'test')

    def test_delete_worker(self):
        worker2 = Worker.objects.get(name='test2')
        worker2.delete()
        self.assertEqual(Worker.objects.count(), 1)
        self.assertNotEqual(Worker.objects.count(), 2)

class WorkerFormTestCase(TestCase):
    
    def test_is_invalid(self):
        form = WorkerForm(data={
            'name': '',
            'contact_info': '',
            'role': '',
        })
        self.assertFalse(form.is_valid())

    def test_is_valid(self):
        form = WorkerForm(data={
            'name': 'test',
            'contact_info': 'test',
            'role': 'test',
        })
        self.assertTrue(form.is_valid())

class WorkerApiTestCase(TestCase):

    def setUp(self):
        self.worker = Worker.objects.create(
            name='testAPI',
            contact_info='testAPI',
            role='testAPI',
        )
    
    # get all workers
    def test_get_all_workers(self):
        response = self.client.get('/api/workers')
        self.assertEqual(response.status_code, 200)

    def test_get_all_workers_with_params(self):
        response = self.client.get('/api/workers', {
            'name': 'testAPI',
            'role': 'testAPI',
        })
        self.assertEqual(response.status_code, 200)
    
    def test_worker_found(self):
        response = self.client.get('/api/workers?name=testAPI')
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_worker_not_found(self):
        response = self.client.get('/api/workers?name=testAPI3')
        self.assertEqual(len(response.data['results']), 0)
    
    # create a worker
    def test_post_worker(self):
        response = self.client.post(path='/api/worker', data={
            'name': 'testAPI2',
            'contact_info': 'testAPI2',
            'role': 'testAPI2',
        }, content_type='application/json', data_type='json')
        self.assertEqual(response.status_code, 201)
        self.assertDictContainsSubset(response.data, {
            'name': 'testAPI2',
            'contact_info': 'testAPI2',
            'role': 'testAPI2',
        })

    # get a worker by id
    def test_get_worker(self):
        id = self.worker.id
        response = self.client.get(f'/api/worker/{id}')
        self.assertEqual(response.status_code, 200)
        
    # update a worker by id
    def test_put_worker(self):
        id = self.worker.id
        response = self.client.put(path=f'/api/worker/{id}', data={
            'name': 'testAPI2',
            'contact_info': 'testAPI2',
            'role': 'testAPI2',
        }, content_type='application/json', data_type='json')
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(response.data, {
            'id': id,
            'name': 'testAPI2',
            'contact_info': 'testAPI2',
            'role': 'testAPI2',
        })
    
    # delete a worker by id
    def test_delete_worker(self):
        id = self.worker.id
        response = self.client.delete(f'/api/worker/{id}')
        self.assertEqual(response.status_code, 200)

from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from .models import Employee

# Create your tests here.
class PeopleDataTests(TestCase):
    def test_people_app_home(self):
        url = reverse("people_data_home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_people_app_add(self):
        url = reverse("add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class DatabasePeopleDataTest(TransactionTestCase):
    def setUp(self):
        # Create an Employee object for testing
        self.employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            address='123 Main St',
            phone='1234567890',
            email='john@example.com',
            emergency_contact='Jane Doe',
            employment_start_date='2023-01-01',
        )

    def tearDown(self):
        # Clean up the Employee object created during the test
        self.employee.delete()

    def test_people_app_edit(self):
        url = reverse("edit", kwargs={'id': self.employee.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_people_app_view_employee(self):
        url = reverse("edit", kwargs={'id': self.employee.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_people_app_deleteemployee(self):
        url = reverse("delete", kwargs={'id': self.employee.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
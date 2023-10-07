from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_app_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_app_operation(self):
        response = self.client.get("/operation/")
        self.assertEqual(response.status_code, 200)

    def test_home_app_customers(self):
        response = self.client.get("/customers/")
        self.assertEqual(response.status_code, 200)

    def test_home_app_finance(self):
        response = self.client.get("/finance/")
        self.assertEqual(response.status_code, 200)

    def test_home_app_projects(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)

    def test_home_app_KPIs(self):
        response = self.client.get("/KPIs/")
        self.assertEqual(response.status_code, 200)

    def test_home_app_about(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_app_people(self):
        response = self.client.get("/people/")
        self.assertEqual(response.status_code, 200)

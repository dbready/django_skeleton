from django.test import TestCase


class CoreViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_is_healthy(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

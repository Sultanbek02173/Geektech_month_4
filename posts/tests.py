from django.test import TestCase, Client
from django.urls import reverse

class HelloTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        responce = self.client.get(reverse("hello-view"))
        expected_data = "<h1>Hello</h1>"
        expected_header = "Alex"

        self.assertEqual(responce.content.decode(), expected_data)
        self.assertEqual(responce.status_code, 500)
        self.assertEqual(responce.headers["name"], expected_header)


    def test_get_index(self):
        responce = self.client.get(reverse("index-page"))

        self.assertTemplateUsed(responce, "posts/index.html")
        self.assertEqual(responce.status_code, 200)


    def test_get_contacts(self):
        responce = self.client.get(reverse("contacts-view"))

        self.assertTemplateUsed(responce, "posts/contacts.html")
        self.assertEqual(responce.status_code, 200)


    def test_get_about(self):
        responce = self.client.get(reverse("about-view"))

        self.assertTemplateUsed(responce, "posts/about.html")
        self.assertEqual(responce.status_code, 200)
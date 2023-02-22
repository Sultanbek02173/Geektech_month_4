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
        responce_get = self.client.get(reverse("index-page"))
        responce_post = self.client.post(reverse("index-page"))

        expect_get = "Главная страница"
        expect_post = "Не тот запрос"

        self.assertEqual(responce_get.status_code, 200)
        self.assertEqual(responce_post.status_code, 200)
        self.assertEqual(responce_get.content.decode(), expect_get)
        self.assertEqual(responce_post.content.decode(), expect_post)



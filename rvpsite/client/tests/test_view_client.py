from django.test import TestCase
from django.shortcuts import resolve_url as r
from rvpsite.client.forms import LoginForm


class ClientGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('new_clients'))

    def test_get(self):
        """GET /clientes/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use clients/clients_form.html"""
        self.assertTemplateUsed(self.response, 'clients/clients_form.html')

    def test_html(self):
        """HTML must contain input tags"""
        tags = (('<form', 1),
                ('<input', 3),
                ('type="submit"', 1))

        for tag,count in tags:
            with self.subTest():
                self.assertContains(self.response, tag, count)

    def test_csrf(self):
        """HTML must contain CSRF"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """"Context must have login form"""
        form = self.response.context['form']
        self.assertIsInstance(form, LoginForm)

    def test_form_has_fields(self):
        """Form must have 2 fields"""
        form = self.response.context['form']

        self.assertSequenceEqual(['email', 'password'], list(form.fields))

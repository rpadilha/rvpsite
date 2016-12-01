from django.test import TestCase
from rvpsite.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp (self):
        self.response = self.client.get('/cadastro/')

    def test_get (self):
        """GET /cadastro/ must return status code 200"""
        response = self.client.get('/cadastro/')
        self.assertEqual(200, self.response.status_code)

    def test_template (self):
        """Must use subscriptions/subscription_form.html"""
        response = self.client.get('/cadastro/')
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """"HTML must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 12)
        self.assertContains(self.response, 'type="text"', 9)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, '<select', 2)
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """"HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """"Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """"Form must have 10 fields """
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cnpj', 'insc_estadual', 'phone', 'email', 'address', 'neighborhood',
                                  'city', 'state', 'zip', 'password', 'password_confirmation'],
                                 list(form.fields))

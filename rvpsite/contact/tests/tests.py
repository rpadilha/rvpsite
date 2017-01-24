from django.core import mail
from django.test import TestCase
from rvpsite.contact.forms import ContactForm

class ContactMessageTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/contato/')

    def test_get(self):
        """GET /contato/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use contact/contact_form.html"""
        self.assertTemplateUsed(self.response, 'contacts/contact_form.html')

    def test_html(self):
        """"HTML must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 4)
        self.assertContains(self.response, '<textarea')
        self.assertContains(self.response, '<label', 4)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="submit"')
        self.assertContains(self.response, 'type="reset"')

    def test_csrf(self):
        """"HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """"Context must have contact form"""
        form = self.response.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_form_has_fields(self):
        """"Form must have 5 fields """
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'email', 'phone', 'msg', 'ipaddr'], list(form.fields))


class ContactMessagePostTest(TestCase):
    def setUp(self):
        data = dict(name='Renato Padilha', email='tonare@gmail.com',
                    phone='21988010276', msg='Como faço para realizar pedidos fora do horário comercial?')
        self.response = self.client.post('/contato/', data)

    def test_post(self):
        """Valid POST should redirect to /contato/"""
        self.assertEqual(302, self.response.status_code)

    def test_send_contact_email(self):
        """1 email should be sent"""
        self.assertEqual(1, len(mail.outbox))

    def test_contact_mail_subject(self):
        """E-mail should have an specific subject"""
        email = mail.outbox[0]
        expect = 'Nova mensagem do site'
        self.assertEqual(expect, email.subject)

    def test_contact_mail_sender(self):
        """E-mail should have an specific sender"""
        email = mail.outbox[0]
        expect = 'tonare@gmail.com'
        self.assertEqual(expect, email.from_email)

    def test_contact_mail_to (self):
        """E-mail should have a destination"""
        email = mail.outbox[0]
        expect = ['rvprepresentacao@gmail.com']
        self.assertEqual(expect, email.to)

    def test_contact_mail_body(self):
        """E-mail body should msg info"""
        email = mail.outbox[0]
        self.assertIn('Como faço para realizar pedidos fora do horário comercial?', email.body)


class ContactMessageInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/contato/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contacts/contact_form.html')

    def test_has_form(self):
        """"When we got an error in the form, form should be sent in the context"""
        form = self.response.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_form_has_errors(self):
        """"Errors should be returned through render return"""
        form = self.response.context['form']
        self.assertTrue(form._errors)


class ContactSuccessMessage(TestCase):
    def setUp(self):
        self.data = dict(name='Renato Padilha', email='tonare@gmail.com',
                    phone='21988010276', msg='Como faço para realizar pedidos fora do horário comercial?')

    def test_message(self):
        response = self.client.post('/contato/', self.data, follow=True)
        self.assertContains(response, 'Mensagem enviada com sucesso!')

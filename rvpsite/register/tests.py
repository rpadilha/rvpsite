from django.core import mail
from django.test import TestCase
from rvpsite.register.forms import RegisterForm


class RegisterTest(TestCase):
    def setUp (self):
        self.response = self.client.get('/cadastro/')

    def test_get (self):
        """GET /cadastro/ must return status code 200"""
        response = self.client.get('/cadastro/')
        self.assertEqual(200, self.response.status_code)

    def test_template (self):
        """Must use subscriptions/subscription_form.html"""
        response = self.client.get('/cadastro/')
        self.assertTemplateUsed(self.response, 'registers/register_form.html')

    def test_html(self):
        """"HTML must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 11)
        self.assertContains(self.response, 'type="text"', 8)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, '<select', 2)
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """"HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """"Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, RegisterForm)

    def test_form_has_fields(self):
        """"Form must have 10 fields """
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cnpj', 'insc_estadual', 'phone', 'email', 'contact_person',
                                  'address', 'neighborhood', 'city', 'state', 'zip'],
                                 list(form.fields))


class RegisterPostTest(TestCase):
    def setUp (self):
        data = dict(name='Jovel Materiais de Construção', cnpj='01234567890123',
                    insc_estadual='012345678', phone='21988010276', email='tonare@gmail.com',
                    contact_person='Marcos Roosevelt', address='Avenida Presidente Dutra, 359',
                    neighborhood='Cidade Nova', city='Itaperuna', state='Rio de Janeiro', zip='28300-000')
        self.response = self.client.post('/cadastro/', data)

    def test_post (self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEqual(302, self.response.status_code)

    def test_send_register_email (self):
        """1 email should be sent"""
        self.assertEqual(1, len(mail.outbox))

    def test_register_mail_subject (self):
        """E-mail should have an specific subject"""
        email = mail.outbox[0]
        expect = 'RVP Representação - Confirmação de Cadastro'
        self.assertEqual(expect, email.subject)

    def test_register_mail_sender(self):
        """E-mail should have an specific sender"""
        email = mail.outbox[0]
        expect = 'rvprepresentacao@gmail.com'
        self.assertEqual(expect, email.from_email)

    def test_subscription_mail_to (self):
        """E-mail should have 2 destinations"""
        email = mail.outbox[0]
        expect = ['tonare@gmail.com', 'tonare@gmail.com']
        self.assertEqual(expect, email.to)


class RegisterInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/cadastro/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'registers/register_form.html')

    def test_has_form (self):
        """"When we got an error in the form, form should be sent in the context"""
        form = self.response.context['form']
        self.assertIsInstance(form, RegisterForm)

    def test_form_has_errors (self):
        """"Errors should be returned through render return"""
        form = self.response.context['form']
        self.assertTrue(form._errors)


class RegisterSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='Jovel Materiais de Construção', cnpj='01234567890123',
                    insc_estadual='012345678', phone='21988010276', email='tonare@gmail.com',
                    contact_person='Marcos Roosevelt', address='Avenida Presidente Dutra, 359',
                    neighborhood='Cidade Nova', city='Itaperuna', state='Rio de Janeiro', zip='28300-000')
        response = self.client.post('/cadastro/', data, follow=True)
        self.assertContains(response, 'Cadastro realizado com sucesso!')


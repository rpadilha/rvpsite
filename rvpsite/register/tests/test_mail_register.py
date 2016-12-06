from django.core import mail
from django.test import TestCase


class RegisterPostValid(TestCase):
    def setUp(self):
        data = dict(name='Jovel Materiais de Construção', cnpj='01234567890123',
                    insc_estadual='012345678', phone='21988010276', email='tonare@gmail.com',
                    contact_person='Marcos Roosevelt', address='Avenida Presidente Dutra, 359',
                    neighborhood='Cidade Nova', city='Itaperuna', state='Rio de Janeiro', zip='28300-000')
        self.response = self.client.post('/cadastro/', data)

    def test_register_mail_subject(self):
        """E-mail should have an specific subject"""
        email = mail.outbox[0]
        expect = 'RVP Representação - Confirmação de Cadastro'
        self.assertEqual(expect, email.subject)

    def test_register_mail_from(self):
        """E-mail should have an specific sender"""
        email = mail.outbox[0]
        expect = 'rvprepresentacao@gmail.com'
        self.assertEqual(expect, email.from_email)

    def test_subscription_mail_to(self):
        """E-mail should have 2 destinations"""
        email = mail.outbox[0]
        expect = ['tonare@gmail.com', 'tonare@gmail.com']
        self.assertEqual(expect, email.to)

    def test_subscription_mail_body(self):
        """E-mail body should have subscriptor info"""
        email = mail.outbox[0]
        self.assertIn('Jovel Materiais de Construção', email.body)
        self.assertIn('01234567890123', email.body)
        self.assertIn('012345678', email.body)
        self.assertIn('21988010276', email.body)
        self.assertIn('tonare@gmail.com', email.body)
        self.assertIn('Marcos Roosevelt', email.body)
        self.assertIn('Avenida Presidente Dutra, 359', email.body)
        self.assertIn('Cidade Nova', email.body)
        self.assertIn('Itaperuna', email.body)
        self.assertIn('Rio de Janeiro', email.body)
        self.assertIn('28300-000', email.body)

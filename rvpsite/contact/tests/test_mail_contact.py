from django.core import mail
from django.test import TestCase


class ContactEmailValid(TestCase):
    def setUp(self):
        data = dict(name='Renato Padilha', email='tonare@gmail.com',
                    phone='21988010276', msg='Como faço para realizar pedidos fora do horário comercial?')
        self.response = self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def test_contact_mail_subject(self):
        """E-mail should have an specific subject"""
        expect = 'Nova mensagem do site'
        self.assertEqual(expect, self.email.subject)

    def test_contact_mail_from(self):
        """E-mail should have an specific sender"""
        expect = 'tonare@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_contact_mail_to (self):
        """E-mail should have a destination"""
        expect = ['rvprepresentacao@gmail.com']
        #expect = ['tonare@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_contact_mail_body(self):
        """E-mail body should msg info"""
        contents = ['Renato Padilha', 'tonare@gmail.com', '21988010276',
                    'como faço para realizar pedidos fora do horário comercial?']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

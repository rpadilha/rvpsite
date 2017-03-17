from django.shortcuts import resolve_url as r
from django.test import TestCase

class BlogPreviewsGet(TestCase):
    fixtures = ['blog.json', 'content.json']

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_context_blog_main(self):
        """Blog preview must be in context"""
        main = self.response.context['blog_preview']
        self.assertIsInstance(main, list)

    def test_dinamic_blog_preview(self):
        """Blog preview should be loaded dynamically"""
        preview = 'Não deixe de nos visitar na Feicon Batimat 2017!!'

        self.assertContains(self.response, preview)
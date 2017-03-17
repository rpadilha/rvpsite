from django.shortcuts import resolve_url as r
from django.test import TestCase
from rvpsite.blog.models import Blogs


class BlogGet(TestCase):
    fixtures = ['blog.json', 'content.json']

    def setUp(self):
        self.response = self.client.get(r('blog', category='seja-bem-vindo-ao-portal-da-rvp-representacao'))

    def test_catalogs_generic(self):
        """GET /noticias/catalogos/ must return status code 200"""
        response = self.client.get(r('blog', category=Blogs.CATALOG, page='1'))
        self.assertEqual(200, response.status_code)

    def test_events_generic(self):
        """GET /noticias/eventos/ must return status code 200"""
        response = self.client.get(r('blog', category=Blogs.EVENT, page='1'))
        self.assertEqual(200, response.status_code)

    def test_news_generic(self):
        """GET /noticias/novidades/ must return status code 200"""
        response = self.client.get(r('blog', category=Blogs.NEWS, page='1'))
        """GET /noticias/novidades/ must return status code 200"""
        self.assertEqual(200, response.status_code)

    def test_promo_generic(self):
        """GET /noticias/promocoes/ must return status code 200"""
        response = self.client.get(r('blog', category=Blogs.PROMO, page='1'))
        """GET /noticias/novidades/ must return status code 200"""
        self.assertEqual(200, response.status_code)

    def test_others_generic(self):
        """GET /noticias/outros/ must return status code 200"""
        response = self.client.get(r('blog', category=Blogs.OTHER, page='1'))
        self.assertEqual(200, response.status_code)

    def test_without_page_parameter(self):
        """We also should have success accessing without a PAGE parameter"""
        self.response = self.client.get(r('blog', category=Blogs.NEWS))
        self.assertEqual(200, self.response.status_code)

    def test_without_category_and_page_parameters(self):
        """We also should have success when accessing without a CATEGORY and PAGE parameters"""
        self.response = self.client.get(r('blog'))
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'blogs/blog.html')

    def test_specific_blog(self):
        contents = [
            'Seja bem-vindo ao portal da RVP Representação',
            '1 de Outubro de 2016',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_context_blog_main(self):
        """Blog month must be in context"""
        main = self.response.context['blog']
        self.assertIsInstance(main, Blogs)


class BlogNotFound(TestCase):
    fixtures = ['blog.json', 'content.json']

    def test_not_found(self):
        response = self.client.get(r('blog', category='notfound'))
        self.assertEqual(404, response.status_code)

    def test_publish_is_false(self):
        """Blog should show 404 when model field PUBLISH == False"""
        response = self.client.get(r('blog', category='promocao-gamma-ferramentas-fevereiro17'))
        self.assertEqual(404, response.status_code)

    def test_invalid_pages(self):
        response = self.client.get('/noticias/asdf/asdf/asdf')
        self.assertEqual(404, response.status_code)


class CategoriesFullBlog(TestCase):
    fixtures = ['blog.json', 'content.json']

    def test_catalog_without_page_parameter(self):
        response = self.client.get(r('blog', category=Blogs.CATALOG))
        contents = [
            'Catálogos',
            'Não existe conteúdo cadastrado para esta categoria',
            '10 de Outubro de 2016',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(response, expected)

    def test_catalog_with_page_parameter(self):
        response = self.client.get(r('blog', category=Blogs.NEWS, page='3'))
        contents = [
            'Seja bem-vindo ao portal da RVP Representação!',
            'seja-bem-vindo-ao-portal-da-rvp-representacao',
            '1 de Outubro de 2016',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(response, expected)

    def test_show_previous_link(self):
        """Blog should have a previous button to the previous blog page"""
        response = self.client.get(r('blog', category=Blogs.NEWS, page='2'))
        content = 'previous.png'

        self.assertContains(response, content)

    def test_show_next_link(self):
        """Blog should have a next button to the next blog page"""
        response = self.client.get(r('blog', category=Blogs.NEWS, page='1'))
        content = 'next.png'

        self.assertContains(response, content)

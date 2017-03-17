from django.test import TestCase
from rvpsite.blog.models import Blogs, Contents


class ContentsGet(TestCase):
    def setUp(self):
        self.title = Blogs.objects.create(
            title = 'Nova Notícia',
            publish = True,
            slug = 'nova-noticia'
        )

    def test_create(self):
        content = Contents.objects.create(
            title = self.title,
            order_out = 1,
            text = 'Você não pode perder a mais nova promoção da Gamma!',
            picture = 'blogpicture.png',
            inverse = False
        )
        self.assertTrue(Contents.objects.exists())

    def test_order_out_cant_be_blank(self):
        field = Contents._meta.get_field('order_out')
        self.assertFalse(field.blank)

    def test_str(self):
        content = Contents(
            title=self.title,
            order_out=1,
            text='Você não pode perder a mais nova promoção da Gamma!',
            picture='blogpicture.png',
            inverse=False
        )
        self.assertEqual('1', str(content))


# O código abaixo deverão ser utilizados na validação do form Django
# FORMS.py do ADMIM
#         class ContentForm(forms.ModelForm):
#             class Meta:
#                 model = Contents
#                 fields = ['order_out', 'text', 'picture', 'inverse']
#
#             def clean (self):
#                 if not self.cleaned_data.get('get') and not self.cleaned_data.get('picture'):
#                     raise ValidationError('Informe um TEXTO ou carregue uma IMAGEM!')
#                 return self.cleaned_data
#
# TESTS.py
#     def test_text_picture_blank_together(self):
#         '''Text and Picture can't be blank together'''
#         form = self.make_validated_form(text='', picture='')
#         self.assertListEqual(['__all__'], list(form.errors))
#
#
# ## As funções abaixo foram criadas para auxiliar na execução dos testes
#
#     def make_validated_form(self, **kwargs):
#         VALID = dict(title=self.title,
#                      order_out=1,
#                      text='Novo texto',
#                      picture='imagem.jpg',
#                      inverse=False)
#
#         data = dict(VALID, **kwargs)
#         form = ContentForm(data)
#         form.is_valid()
#         return form
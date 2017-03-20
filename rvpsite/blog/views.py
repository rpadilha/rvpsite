from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from math import ceil
from rvpsite.blog.models import Blogs
from django.views.generic import FormView
from .forms import S3DirectUploadForm


def blog(request, category, page):
    if request.method == 'POST':
        # Será usando para processar a pesquisa por notícias
        pass
    elif request.method == 'GET':
        # IF CATEGORY está entre ['geral', 'catalogos', 'eventos', 'novidades', 'promocoes', 'outros', None]
        # Será mostrada uma página de notícias (independente de categoria)
        if category in ['geral', Blogs.CATALOG, Blogs.EVENT, Blogs.NEWS, Blogs.PROMO, Blogs.OTHER, None]:
            return showFullBlogPage(request, category, page)

        # Caso contrário, será mostrada uma notícia específica
        else:
            raise Http404


def one_blog(request, slug):
    return showEspecificBlog(request, slug)


#######################
## Support Functions ##
#######################
def showEspecificBlog(request, slug):
    blog = get_object_or_404(Blogs.objects.prefetch_related('contents_set').filter(publish=True), slug=slug)
    return render(request, 'blogs/blog.html', {'blog': blog})


def showFullBlogPage(request, category, page):
    if category is None:
        category = 'geral'

    qs = Blogs.objects.prefetch_related('contents_set').filter(publish=True)

    if not category == 'geral':
        qs = qs.filter(category = category)

    if page is None:
        page = 1
    else:
        try:
            page = int(page)
        except:
            raise Http404

    # Slice no QS para mostrar apenas os 5 registros referentes à página que está sendo acessada
    categorized_blogs = get_list_or_404(qs[5*(page-1):5*page])

    stats = get_blog_stats(category, qs.count(), page)
    return render(request, 'blogs/categories.html', {'categorized_blogs': categorized_blogs, 'stats': stats})


def get_blog_stats(category, blogs, page):
    stats = {'total': blogs, 'actual_page': page, 'total_pages': ceil(blogs/5)}

    if page == 1:
        stats['previous'] = False
    else:
        stats['previous'] = True
        if category is None:
            stats['previous_link'] = Blogs.BLOG_DIR + str(page - 1) + '/'
        else:
            stats['previous_link'] = Blogs.BLOG_DIR + category + '/' + str(page-1) + '/'

    if page*5 < blogs:
        stats['next'] = True
        if category is None:
            stats['next_link'] = Blogs.BLOG_DIR + str(page + 1) + '/'
        else:
            stats['next_link'] = Blogs.BLOG_DIR + category + '/' + str(page+1) + '/'
    else:
        stats['next'] = False

    return stats


def _get_blog_months():
    values = []
    qs = Blogs.objects.all()

    for blog in qs:
        values.append(str(blog.created_at.year) + '/' + str(blog.created_at.month))

    return remove_duplicates(values)


def remove_duplicates (values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


class MyView(FormView):
    template_name = 'form.html'
    form_class = S3DirectUploadForm


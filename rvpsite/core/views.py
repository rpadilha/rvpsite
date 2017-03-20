from django.shortcuts import render
from re import match
from rvpsite.blog.models import Blogs


def home(request):
    blog_preview = get_blog_preview()
    return render(request, 'index.html', {'blog_preview': blog_preview})


def area(request):
    return render(request, 'area.html')


def representations(request):
    return render(request, 'representations.html')


#######################
## SUPPORT FUNCTIONS ##
#######################
def get_blog_preview():
    """This function should return a dict with the last 3 blog previews to the home view"""
    blog_preview = []
    qs = Blogs.objects.prefetch_related('contents_set').filter(publish=True)

    for blog in qs[0:3]:
        content = {}

        content['title'] = blog.title
        content['slug'] = blog.slug

        for blogcontent in blog.contents_set.all():
            temp_str = blogcontent.text

            if len(temp_str) > 0:
                content['preview'] = match(r'^([\w ]{,60}[.!?]*){1,3}', temp_str).group()
                break

        blog_preview.append(content)

    return blog_preview
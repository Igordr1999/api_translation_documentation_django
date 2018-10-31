from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils.translation import activate
from django.shortcuts import render
from news.models import Article, Blog
from news.serializers import BlogSerializer
from rest_framework import viewsets


def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)


def article(request, number):
    title = Article.objects.get(id=number).title
    return HttpResponse(title)


def change_lang(request, code):
    request.session[LANGUAGE_SESSION_KEY] = code
    return HttpResponse("OK")


def about(request):
    return render(request, "about.html")


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


from django.http import HttpResponse, JsonResponse
def getAll(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Blog.objects.all()
        serializer = BlogSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

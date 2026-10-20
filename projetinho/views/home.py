from django.shortcuts import render
from django.conf import settings
from projetinho.models import Post


def home(request):
    posts = Post.objects.all()
    
    context = {
        'tag_title': f'{settings.SITENAME}',
        'posts': posts
    }

    return render(
        request,
        'projetinho/home.html',
        context
    )

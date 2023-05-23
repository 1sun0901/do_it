from django.shortcuts import render

from blog.models import Post


# Create your views here.
def landing(request):
    return render(
        request,
        'single_pages/landing.html',
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html',
    )

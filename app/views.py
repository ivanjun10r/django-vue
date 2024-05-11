from django.shortcuts import render

from .models import BlogLink


def vue_test(request):
    return render(request, "app/index.html")


def blog_view(request):
    object_list = BlogLink.objects.all()
    return render(request, "app/blog_list.html", {"object_list": object_list})

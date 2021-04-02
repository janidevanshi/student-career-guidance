from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "app/home.html", {})


def blog_view(request, *args, **kwargs):
    return render(request, "app/blog.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "app/contact.html", {})


def faq_view(request, *args, **kwargs):
    return render(request, "app/faq.html", {})


def login_view(request, *args, **kwargs):
    return render(request, "app/login.html", {})


def register_view(request, *args, **kwargs):
    return render(request, "app/register.html", {})

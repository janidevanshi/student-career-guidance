from django.shortcuts import render, HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "app/home.html", {})


def blog_view(request, *args, **kwargs):
    return render(request, "app/blog.html", {})


def contact_view(request, *args, **kwargs):
    if request.method == 'POST':
        print('We are using post request')
    return render(request, "app/contact.html", {})


def faq_view(request, *args, **kwargs):
    return render(request, "app/faq.html", {})

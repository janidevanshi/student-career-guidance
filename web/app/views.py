from django.shortcuts import render, HttpResponse
from app.models import Contact, Post
from django.contrib import messages
# Create your views here.


def home_view(request, *args, **kwargs):
    allPosts = Post.objects.all()
    context = {
        'allPosts': allPosts
    }
    return render(request, "app/home.html", context)


def bloghome_view(request, *args, **kwargs):
    allPosts = Post.objects.all()
    context = {
        'allPosts': allPosts
    }
    return render(request, "app/blog.html", context)


def blogpost_view(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {
        'post': post
    }
    return render(request, 'app/blogpost.html', context)


def contact_view(request, *args, **kwargs):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        print(name, email, content)

        if len(name) < 2 or len(email) < 3 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, content=content)
            contact.save()
            messages.success(
                request, "Your messages has been successfully sent")
    return render(request, "app/contact.html", {})


def faq_view(request, *args, **kwargs):
    return render(request, "app/faq.html", {})


def search_view(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(content__contains=query)
    params = {'allPosts': allPosts, 'query': query}
    return render(request, "app/search.html", params)

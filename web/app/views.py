from django.shortcuts import render, HttpResponse, redirect
from app.models import Contact, Post, Faq
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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


def blogsearch_view(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(content__contains=query)
    params = {'allPosts': allPosts, 'query': query}
    return render(request, "app/blogsearch.html", params)


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
    allFaqs = Faq.objects.all()
    context = {
        'allFaqs': allFaqs
    }
    return render(request, "app/faq.html", context)


def faqsearch_view(request):

    query = request.GET['query']
    allFaqs = Faq.objects.filter(question__contains=query)
    params = {'allFaqs': allFaqs, 'query': query}
    return render(request, "app/faqsearch.html", params)


def handleSignup(request):
    # GEt the post parameters
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
    # Check for error inputs
        if not email.endswith("com") and not email.endswith("edu"):
            messages.error(request, "Use email which ends with com or edu")
            return redirect('home')

        if len(username) > 12:
            messages.error(request, "Username must be less than 12 characters")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')
        if len(pass1) < 6 and len(pass1) > 10:
            messages.error(
                request, "Password must be greater than 6 characters and less than 10 chacters")
            return redirect('home')

        if not pass1.isalnum():
            messages.error(
                request, "Password should only contain letters and numbers")
            return redirect('home')

        # if not email.endswith("com"):
        #     messages.error(
        #         request, "Use email which ends with com")
        #     return redirect('home')
    # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404-Not Found')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(
            request, username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('home')


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')

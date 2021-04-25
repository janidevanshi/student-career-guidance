from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('blog/', views.bloghome_view, name='blog'),
    path('blog/<str:slug>', views.blogpost_view, name='blogpost'),
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq_view, name='faq'),
    path('blogsearch/', views.blogsearch_view, name='blogsearch'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('faqsearch/', views.faqsearch_view, name='faqsearch'),
]

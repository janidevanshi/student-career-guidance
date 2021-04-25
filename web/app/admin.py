from django.contrib import admin
from .models import Contact, Post, Faq
# Register your models here.

admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Faq)

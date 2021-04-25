from django.db import models
from datetime import datetime, timedelta


# Create your models here.


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='app/images')
    content = models.TextField()
    slug = models.CharField(max_length=130)

    def __str__(self):
        return self.title


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email


class Faq(models.Model):
    sno = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateTimeField(
        blank=True, default=datetime.now())

    def __str__(self):
        return 'Question is about ' + self.subject

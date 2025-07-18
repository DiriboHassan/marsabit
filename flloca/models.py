from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class HeroFlloca(models.Model):
    address = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    twitter = models.CharField(max_length=40)
    facebook = models.CharField(max_length=40)
    youtube = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='flloca/pics')
    hero_bg = models.ImageField(upload_to='flloca/pics')
    text_1 = models.TextField()
    text_2 = models.TextField()

class OurProjects(models.Model):
     class STATUS_CHOICES(models.TextChoices):
        DRAFT = "D", "Draft"
        PUBLISHED = "P", "Published"

    
     img = models.ImageField(upload_to='flloca/pics')
     title = models.CharField(max_length=200)
     slug =  models.SlugField(max_length=200, unique=False)
     desc = RichTextField()
     location = models.CharField(max_length=100)
     created_date =  models.DateTimeField(default=timezone.now)
     posted_on = models.DateTimeField(default=timezone.now)
     created_date = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
     status =  models.CharField(max_length=10, choices=STATUS_CHOICES.choices, default='Draft')

     def __str__(self):
        return self.title



class DeptHeads(models.Model):
     class STATUS_CHOICES(models.TextChoices):
        DRAFT = "D", "Draft"
        PUBLISHED = "P", "Published"

    
     img = models.ImageField(upload_to='flloca/pics')
     name = models.CharField(max_length=200, unique=True)
     title = models.CharField(max_length=200)
     bio = RichTextField()
     email = models.CharField(max_length=25, blank=True)
     twitter = models.CharField(max_length=40)
     facebook = models.CharField(max_length=40)
     created_date =  models.DateTimeField(default=timezone.now)
     posted_on = models.DateTimeField(default=timezone.now)
     status =  models.CharField(max_length=10, choices=STATUS_CHOICES.choices, default='Draft')

     def __str__(self):
        return self.title




class FllocaGallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='flloca/pics')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Introduction(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='flloca/pics')
    flloca_intro = RichTextField()


class GrievanceSteps(models.Model):
    title = models.CharField(max_length=100)
    grievances = RichTextField()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Document(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Services(models.Model):
     img = models.ImageField(upload_to='pics')
     title = models.TextField()
     intro = RichTextField()

     def publish(self):
            self.published_date = timezone.now()
            self.save()


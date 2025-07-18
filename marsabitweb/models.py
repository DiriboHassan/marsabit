from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class Introduction(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    intro = RichTextField()


class About(models.Model):
    name = models.CharField(max_length=100)
    intro = RichTextField()



class Copyright(models.Model):
    sitename = models.CharField(max_length=100)
    rights_text = models.CharField(max_length=100)
    developed_by = models.CharField(max_length=100)
    developer_link = models.CharField(max_length=100)
    
class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='pics')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PromotionalVideo(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='promovideos/%Y/%m/%d/')
    is_active = models.BooleanField(default=True, help_text="Only one active promotional video is displayed at a time.")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Promotional Videos'

class Partners(models.Model):
   img = models.ImageField(upload_to='pics')
   name = models.CharField(max_length=200)
   link = models.CharField(max_length=200)
   posted_on = models.DateTimeField(default=timezone.now)

   def _str_(self):
        return self.name


class Hero(models.Model):
    address = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    twitter = models.CharField(max_length=40)
    facebook = models.CharField(max_length=40)
    youtube = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='pics')
    hero_bg = models.ImageField(upload_to='pics')
    text_1 = models.TextField()
    text_2 = models.TextField()


class HeroOthers(models.Model):
     title = models.TextField()
     
     hero_bg = models.ImageField(upload_to='pics')
     text_1 = models.TextField()


class Services(models.Model):
     img = models.ImageField(upload_to='pics')
     title = models.TextField()
     intro = RichTextField()

     def publish(self):
            self.published_date = timezone.now()
            self.save()


class News(models.Model):
     class STATUS_CHOICES(models.TextChoices):
        DRAFT = "D", "Draft"
        PUBLISHED = "P", "Published"

    
     img = models.ImageField(upload_to='pics')
     title = models.CharField(max_length=200)
     name =  models.SlugField(max_length=200, unique=True)
     body = RichTextField()
     location = models.CharField(max_length=100)
     created_date =  models.DateTimeField(default=timezone.now)
     posted_on = models.DateTimeField(default=timezone.now)
     posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
     status =  models.CharField(max_length=10, choices=STATUS_CHOICES.choices, default='Draft')

     def __str__(self):
        return self.title



class Projects(models.Model):
     class STATUS_CHOICES(models.TextChoices):
        DRAFT = "D", "Draft"
        PUBLISHED = "P", "Published"

    
     img = models.ImageField(upload_to='pics')
     title = models.CharField(max_length=200)
     name =  models.SlugField(max_length=200, unique=True)
     desc = RichTextField()
     location = models.CharField(max_length=100)
     created_date =  models.DateTimeField(default=timezone.now)
     posted_on = models.DateTimeField(default=timezone.now)
     posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
     status =  models.CharField(max_length=10, choices=STATUS_CHOICES.choices, default='Draft')

     def __str__(self):
        return self.title


class Departments(models.Model):
     class STATUS_CHOICES(models.TextChoices):
        DRAFT = "D", "Draft"
        PUBLISHED = "P", "Published"

    
     img = models.ImageField(upload_to='pics')
     title = models.CharField(max_length=200, default='Title')
     name =  models.SlugField(max_length=200, unique=True)
     about = RichTextField()
     location = models.CharField(max_length=100)
     intouch = models.CharField(max_length=200)
     where = models.CharField(max_length=200)
     address = models.CharField(max_length=200)
     email = models.CharField(max_length=200, blank=True)
     created_date =  models.DateTimeField(default=timezone.now)
     posted_on = models.DateTimeField(default=timezone.now)
     posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
     status =  models.CharField(max_length=10, choices=STATUS_CHOICES.choices, default='Draft')

     def __str__(self):
        return self.title



class Executives(models.Model):
     class STATUS_CHOICES(models.TextChoices):
        DRAFT = "D", "Draft"
        PUBLISHED = "P", "Published"

    
     img = models.ImageField(upload_to='pics')
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

     

class Deptheads(models.Model):
     class STATUS_CHOICES(models.TextChoices):
        DRAFT = "D", "Draft"
        PUBLISHED = "P", "Published"

    
     img = models.ImageField(upload_to='pics')
     name = models.CharField(max_length=200, unique=True)
     title = models.CharField(max_length=200)
     designation = models.CharField(max_length=200)
     bio = RichTextField()
     email = models.CharField(max_length=25, blank=True)
     twitter = models.CharField(max_length=40)
     facebook = models.CharField(max_length=40)
     created_date =  models.DateTimeField(default=timezone.now)
     posted_on = models.DateTimeField(default=timezone.now)
     status =  models.CharField(max_length=10, choices=STATUS_CHOICES.choices, default='Draft')

     def __str__(self):
        return self.title



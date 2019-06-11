from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from autoslug import AutoSlugField

gender_choices = [
    ('M', 'Male'),
    ('F', 'Female')
]

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = HTMLField(blank=True, default=u'')
    promo_url = models.URLField(blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    key = AutoSlugField(populate_from='title', unique_with=['name', 'creation_date'])
    password = models.CharField(max_length=150, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    company_logo = models.ImageField(default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    designation = models.CharField(max_length=50, blank=True, null=True)
    descripsion = models.TextField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=gender_choices, default='None', null=True, blank=True)
    profile_pic = models.ImageField(default='', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)


class AboutUs(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=True, blank=True)
    details = HTMLField(blank=True, default=u'')
    mission = HTMLField(blank=True, default=u'')
    vission = HTMLField(blank=True, default=u'')
    mosaic = HTMLField(blank=True, default=u'')
    image = models.ImageField(default='about_us.jpg', blank=True, null=True)


class Services(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    details = HTMLField(blank=True, default=u'')


class Blog(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    descripsion = HTMLField(blank=True, default=u'')
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='', blank=True, null=True)


class ClientReview(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=50, blank=True, null=True)
    review = models.TextField(max_length=500)
    image = models.ImageField(default='', blank=True, null=True)


class AnimationView(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    header = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    descripsion = models.TextField(max_length=500, blank=True, null=True)
    backgroun_image = models.ImageField(default='', blank=True, null=True)


class InteriorDesignImage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(default='')

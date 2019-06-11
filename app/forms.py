from django.forms import ModelForm
from .models import Company, Customer, InteriorDesignImage, AboutUs, Services, Blog, ClientReview, AnimationView
from django import forms


class CompanyRegisterForm(ModelForm):

    class Meta:
        model = Company
        exclude = []


class CustomerRegisterForm(ModelForm):


    class Meta:
        model = Customer

        exclude = []


class InteriorDesignImageForm(ModelForm):
    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = InteriorDesignImage
        exclude = ['company']


class AboutUsForm(ModelForm):
    class Meta:
        model = AboutUs
        exclude = ['company']


class ServicesForm(ModelForm):
    class Meta:
        model = Services
        exclude = ['company']


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ['company']


class ClientReviewForm(ModelForm):
    class Meta:
        model = ClientReview
        exclude = ['company']


class AnimationForm(ModelForm):
    class Meta:
        model = AnimationView
        exclude = ['company']

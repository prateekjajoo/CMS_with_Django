from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect
from .forms import CompanyRegisterForm, CustomerRegisterForm, InteriorDesignImageForm, AboutUsForm, ServicesForm
from .forms import BlogForm, ClientReviewForm, AnimationForm
from django.contrib.auth import authenticate, login, logout
from .models import Customer, Company, InteriorDesignImage, AboutUs, Services, Blog, ClientReview, AnimationView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User

from django.contrib import messages


# Create your views here.

class DasboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class LogoutView(TemplateView):

    def get(self, request, *args, **kwargs):
        request.session['company'] = None
        logout(request)
        return render(request, 'login.html')


class CompanyLogin(TemplateView):
    template_name = "company_login.html"

    def get(self, request, *args, **kwargs):
        if 'company' in request.session:
            return HttpResponseRedirect(reverse('create_aboutus'))
        else:
            return render(request, 'company_login.html')

    def post(self, request):
        user_id = request.POST['user_id']
        user_password = request.POST['password']
        company = Company.objects.values_list().get(email=user_id, password=user_password)
        company = list(company)
        if company is not None:
            del company[8]
            request.session['company'] = company
            return redirect('create_aboutus')

        else:
            messages.add_message(self.request, messages.SUCCESS, "Invalid User Id Password")
            return render(request, "company_login")


class LoginView(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dasboard'))
        else:
            return render(request, 'login.html')

    def post(self, request):
        user_id = request.POST['user_id']
        user_password = request.POST['password']
        user = authenticate(username=user_id, password=user_password)

        if user is not None:
            login(request, user)
            return redirect('dasboard')

        else:
            messages.add_message(self.request, messages.SUCCESS, "Invalid User Id Password")
            return render(request, "login.html")


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyRegisterForm
    template_name = 'company_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Company has been saved successfully !')
        return reverse("add_company")


class CompanyListView(LoginRequiredMixin, ListView):
    template_name = 'company_list.html'
    model = Company


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyRegisterForm
    template_name = 'company_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Company Update successfully !')
        return reverse("list_company")


class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company

    def get(self, request, *args, **kwargs):
        Company.objects.get(id=self.get_object().id).delete()
        messages.add_message(self.request, messages.SUCCESS, 'successfully Delete Company!')
        return HttpResponseRedirect(reverse('list_company'))

    def post(self, request, *args, **kwargs):
        some_var = request.POST.getlist('check')
        Company.objects.filter(id__in=some_var).delete()
        messages.add_message(self.request, messages.SUCCESS, 'successfully Delete Company!')
        return HttpResponseRedirect(reverse('list_company'))


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerRegisterForm
    template_name = 'customer_form.html'

    def form_valid(self, form):
        customer_obj = form.save(commit=False)
        if 'company' in self.request.session:
            customer_obj = form.save(commit=False)
            print(self.request.session['company'])
            if form.is_valid():
                customer_obj.company_id = self.request.session['company'][0]

        customer_obj.save()

        messages.add_message(self.request, messages.SUCCESS, 'Customer has been saved successfully!')
        return HttpResponseRedirect(reverse('add_customer'))


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer_list.html'


class CustomerDatalistView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer_data_list.html'


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerRegisterForm
    template_name = 'customer_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Customer Update successfully !')
        return reverse("list_customer")


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer

    def get(self, request, *args, **kwargs):
        Customer.objects.get(id=self.get_object().id).delete()
        messages.add_message(self.request, messages.SUCCESS, 'successfully Delete Customer!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def post(self, request, *args, **kwargs):
        some_var = request.POST.getlist('check')
        Customer.objects.filter(id__in=some_var).delete()
        messages.add_message(self.request, messages.SUCCESS, 'successfully Delete Customer!')
        return HttpResponseRedirect(reverse('list_customer'))


class WebsideIndex(TemplateView):
    template_name = 'web/index.html'

    def get(self, request, *args, **kwargs):
        company_key = self.kwargs['company_key']
        company_id = self.kwargs['pk']
        company = Company.objects.get(key=company_key, id=company_id)
        return render(request, 'web/index.html', {'company': company})


class WebsideAbout(TemplateView):
    template_name = 'web/about.html'

    def get(self, request, *args, **kwargs):
        company_key = self.kwargs['company_key']
        company_id = self.kwargs['pk']
        company = Company.objects.get(key=company_key, id=company_id)
        return render(request, 'web/about.html', {'company': company})


class WebsideProject(TemplateView):
    template_name = 'web/project.html'

    def get(self, request, *args, **kwargs):
        company_key = self.kwargs['company_key']
        company_id = self.kwargs['pk']
        company = Company.objects.get(key=company_key, id=company_id)
        return render(request, 'web/project.html', {'company': company})


class WebsideServices(TemplateView):
    template_name = 'web/services.html'

    def get(self, request, *args, **kwargs):
        company_key = self.kwargs['company_key']
        company_id = self.kwargs['pk']
        company = Company.objects.get(key=company_key, id=company_id)
        return render(request, 'web/services.html', {'company': company})


class WebsideTeam(TemplateView):
    template_name = 'web/team.html'

    def get(self, request, *args, **kwargs):
        company_key = self.kwargs['company_key']
        company_id = self.kwargs['pk']
        company = Company.objects.get(key=company_key, id=company_id)
        return render(request, 'web/team.html', {'company': company})


class WebsideBlog(TemplateView):
    template_name = 'web/blog.html'

    def get(self, request, *args, **kwargs):
        company_key = self.kwargs['company_key']
        company_id = self.kwargs['pk']
        company = Company.objects.get(key=company_key, id=company_id)
        return render(request, 'web/blog.html', {'company': company})


class WebsideContect(TemplateView):
    template_name = 'web/comtect.html'

    def get(self, request, *args, **kwargs):
        company_key = self.kwargs['company_key']
        company_id = self.kwargs['pk']
        company = Company.objects.get(key=company_key, id=company_id)
        return render(request, 'web/contact.html', {'company': company})


class WebsideBlogSingle(TemplateView):
    template_name = 'web/blog-single.html'

    def get(self, request, *args, **kwargs):
        company_key = self.kwargs['company_key']
        company_id = self.kwargs['pk']
        company = Company.objects.get(key=company_key, id=company_id)
        return render(request, 'web/blog-single.html', {'company': company})


class InteriorDesignImageCreateView(CreateView):
    model = InteriorDesignImage
    form_class = InteriorDesignImageForm
    template_name = "web/upload_file.html"

    def post(self, request, *args, **kwargs):
        image_list = request.FILES.getlist('image')
        for img in image_list:
            obj = InteriorDesignImage(company_id=self.request.session['company'][0], image=img)
            obj.save()
        messages.add_message(self.request, messages.SUCCESS, 'All Images uploaded successfully !')
        return HttpResponseRedirect(reverse('Interior_Design_Image'))

    def get(self, request, *args, **kwargs):
        image_list = InteriorDesignImage.objects.all()
        return render(request, "web/upload_file.html", {'image_list': image_list, 'form':InteriorDesignImageCreateView.form_class})


class InteriorDesignImageDeleteView(DeleteView):
    model = InteriorDesignImage

    def get(self, request, *args, **kwargs):
        InteriorDesignImage.objects.get(id=self.get_object().id).delete()
        messages.add_message(self.request, messages.SUCCESS, 'successfully Delete Image!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AboutUsCreateView(CreateView):
    model = AboutUs
    form_class = AboutUsForm
    template_name = 'aboutus_form.html'

    def form_valid(self, form):
        about_obj = form.save(commit=False)
        print(self.request.session['company'])
        if form.is_valid():
            about_obj.company_id = self.request.session['company'][0]
            about_obj.save()
            messages.add_message(self.request, messages.SUCCESS, 'About Us Saved ')
            return HttpResponseRedirect(reverse("add_company"))


class ServicesCreateView(CreateView):
    model = Services
    form_class = ServicesForm
    template_name = 'services_form.html'

    def get(self, request, *args, **kwargs):
        services_list = Services.objects.all()
        return render(request, "services_form.html",
                      {'services_list': services_list, 'form': ServicesCreateView.form_class})

    def form_valid(self, form):
        services_obj = form.save(commit=False)
        print(self.request.session['company'])
        if form.is_valid():
            services_obj.company_id = self.request.session['company'][0]
            services_obj.save()
            messages.add_message(self.request, messages.SUCCESS, 'Services has been added successfully !')
            return HttpResponseRedirect(reverse("create_services"))


class ServicesUpdateView(UpdateView):
    model = Services
    form_class = ServicesForm
    template_name = 'services_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Services Update successfully !')
        return reverse("create_services")


class ServicesDeleteView(DeleteView):
    model = Services

    def get(self, request, *args, **kwargs):
        Services.objects.get(id=self.get_object().id).delete()
        messages.add_message(self.request, messages.SUCCESS, 'successfully Delete Services!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_form.html'

    def form_valid(self, form):
        blog = form.save(commit=False)
        print(self.request.session['company'])
        if form.is_valid():
            blog.company_id = self.request.session['company'][0]
            blog.save()
            messages.add_message(self.request, messages.SUCCESS, 'Blog has been added successfully !')
            return HttpResponseRedirect(reverse("create_blog"))

    def get(self, request, *args, **kwargs):
        blog_list = Blog.objects.all()
        return render(request, "blog_form.html",
                      {'blog_list': blog_list, 'form': BlogCreateView.form_class})


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Blog Update successfully !')
        return reverse("create_blog")


class BlogDeleteView(DeleteView):
    model = Blog

    def get(self, request, *args, **kwargs):
        Blog.objects.get(id=self.get_object().id).delete()
        messages.add_message(self.request, messages.SUCCESS, 'successfully Delete Blog!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ClientReviewCreateView(CreateView):
    model = ClientReview
    form_class = ClientReviewForm
    template_name = 'clientreview_form.html'

    def form_valid(self, form):
        client_review = form.save(commit=False)
        print(self.request.session['company'])
        if form.is_valid():
            client_review.company_id = self.request.session['company'][0]
            client_review.save()
            messages.add_message(self.request, messages.SUCCESS, 'Client Review has been added successfully !')
            return HttpResponseRedirect(reverse("create_client_review"))

    def get(self, request, *args, **kwargs):
        client_list = ClientReview.objects.all()
        return render(request, "clientreview_form.html",
                      {'client_list': client_list, 'form': ClientReviewCreateView.form_class})


class ClientReviewUpdateView(UpdateView):
    model = ClientReview
    form_class = ClientReviewForm
    template_name = 'clientreview_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Client Review Update successfully !')
        return reverse("create_client_review")


class ClientReviewDeleteView(DeleteView):
    model = ClientReview

    def get(self, request, *args, **kwargs):
        ClientReview.objects.get(id=self.get_object().id).delete()
        messages.add_message(self.request, messages.SUCCESS, 'successfully Delete Client Review!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AnimationCreateView(CreateView):
    model = AnimationView
    form_class = AnimationForm
    template_name = 'animationview_form.html'

    def get(self, request, *args, **kwargs):
        animation_list = AnimationView.objects.all()
        return render(request, "animationview_form.html",
                      {'animation_list': animation_list, 'form': AnimationCreateView.form_class})

    def form_valid(self, form):
        animation_obj = form.save(commit=False)
        print(self.request.session['company'])
        if form.is_valid():
            animation_obj.company_id = self.request.session['company'][0]
            animation_obj.save()
            messages.add_message(self.request, messages.SUCCESS, 'Animation View has been added successfully !')
            return HttpResponseRedirect(reverse("create_animation"))


class AnimationUpdateView(UpdateView):
    model = AnimationView
    form_class = AnimationForm
    template_name = 'animationview_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Animation Update successfully !')
        return reverse("create_animation")


class AnimationDeleteView(DeleteView):
    model = AnimationView

    def get(self, request, *args, **kwargs):
        AnimationView.objects.get(id=self.get_object().id).delete()
        messages.add_message(self.request, messages.SUCCESS, 'successfully Delete Animation View!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

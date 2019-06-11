from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import DasboardView, LoginView, LogoutView, CustomerDatalistView, InteriorDesignImageCreateView
from .views import CompanyCreateView, CompanyListView, CompanyUpdateView, CompanyDeleteView, AnimationCreateView
from .views import CustomerCreateView, CustomerListView, CustomerUpdateView, CustomerDeleteView, AnimationDeleteView
from .views import WebsideIndex, WebsideAbout, WebsideBlog, WebsideBlogSingle, WebsideContect, ServicesUpdateView
from .views import WebsideProject, WebsideServices, WebsideTeam, InteriorDesignImageDeleteView, AboutUsCreateView
from .views import ServicesCreateView, ServicesDeleteView, BlogCreateView, BlogDeleteView, ClientReviewCreateView, ClientReviewDeleteView
from .views import BlogUpdateView, ClientReviewUpdateView, AnimationUpdateView, CompanyLogin
urlpatterns = [

    path('dasboard', DasboardView.as_view(), name='dasboard'),
    path('', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('create_company', CompanyCreateView.as_view(), name='add_company'),
    path('list-com', CompanyListView.as_view(), name='list_company'),
    path('update-com/<int:pk>', CompanyUpdateView.as_view(), name='update_company'),
    path('del-com/<int:pk>', CompanyDeleteView.as_view(), name='delete_company'),
    path('create_customer', CustomerCreateView.as_view(), name='add_customer'),
    path('list-cus', CustomerListView.as_view(), name='list_customer'),
    path('datalist', CustomerDatalistView.as_view(), name='customer_datalist'),
    path('update-cus/<int:pk>', CustomerUpdateView.as_view(), name='update_customer'),
    path('del-cus/<int:pk>', CustomerDeleteView.as_view(), name='delete_customer'),
    path('web/<slug:company_key>/<int:pk>', WebsideIndex.as_view(), name='web_index'),
    path('<slug:company_key>/<int:pk>/about', WebsideAbout.as_view(), name='web_about'),
    path('<slug:company_key>/<int:pk>/project', WebsideProject.as_view(), name='web_project'),
    path('<slug:company_key>/<int:pk>/services', WebsideServices.as_view(), name='web_service'),
    path('<slug:company_key>/<int:pk>/team', WebsideTeam.as_view(), name='web_team'),
    path('<slug:company_key>/<int:pk>/blog', WebsideBlog.as_view(), name='web_blog'),
    path('<slug:company_key>/<int:pk>/contect', WebsideContect.as_view(), name='web_contect'),
    path('<slug:company_key>/<int:pk>/blog-single', WebsideBlogSingle.as_view(), name='web_blog_single'),
    path('upload-image', InteriorDesignImageCreateView.as_view(), name='Interior_Design_Image'),
    path('image_delete/<int:pk>', InteriorDesignImageDeleteView.as_view(), name='Interior_Image_delete'),
    path('create-aboutus', AboutUsCreateView.as_view(), name='create_aboutus'),
    path('create-services', ServicesCreateView.as_view(), name='create_services'),
    path('update-services/<int:pk>', ServicesUpdateView.as_view(), name='update_services'),
    path('delete-services/<int:pk>', ServicesDeleteView.as_view(), name='delete_services'),
    path('create-blog', BlogCreateView.as_view(), name='create_blog'),
    path('update-blog/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    path('delete-blog/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('create-client', ClientReviewCreateView.as_view(), name='create_client_review'),
    path('update-client/<int:pk>', ClientReviewUpdateView.as_view(), name='update_client_review'),
    path('delete-client/<int:pk>', ClientReviewDeleteView.as_view(), name='delete_client_review'),
    path('create-animation', AnimationCreateView.as_view(), name='create_animation'),
    path('update-animation/<int:pk>', AnimationUpdateView.as_view(), name='update_animation'),
    path('delete-animation/<int:pk>', AnimationDeleteView.as_view(), name='delete_animation'),
    path('company-login', CompanyLogin.as_view(), name='company_login'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

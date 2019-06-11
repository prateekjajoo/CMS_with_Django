from django.contrib import admin
from .models import Company, Customer, AboutUs, Blog, Services, ClientReview, AnimationView, InteriorDesignImage

# Register your models here.

admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(AboutUs)
admin.site.register(Blog)
admin.site.register(Services)
admin.site.register(ClientReview)
admin.site.register(AnimationView)
admin.site.register(InteriorDesignImage)

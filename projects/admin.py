from django.contrib import admin

# Register your models here
from .models import Profile, ListProperty, Category

admin.site.register(Profile)
admin.site.register(ListProperty)
admin.site.register(Category)

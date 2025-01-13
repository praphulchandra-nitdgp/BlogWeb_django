from django.contrib import admin
from .models import ProfileModel
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

admin.site.register(ProfileModel)
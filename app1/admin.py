from dataclasses import fields
from django.contrib import admin
from .models import PostData
# Register your models here.
@admin.register(PostData)
class PostDataAdmin(admin.ModelAdmin):
    fields = ['name','image','discription']
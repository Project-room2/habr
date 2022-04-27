from django.contrib import admin
from .models import *


class AdminHabr(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_active', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Habr, AdminHabr)
admin.site.register(Category, AdminCategory)

from django.contrib import admin

from .models import *


class AdminHabr(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_active', 'is_published', 'category', 'habr_view')
    list_display_links = ('id', 'title')
    list_editable = ('is_active', 'is_published', 'category',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    fields = [
        'time_create', 'time_update', 'title', 'slug', 'category', 'content', 'user', 'is_active', 'is_published',
        'likes', ]
    readonly_fields = ('time_create', 'time_update')
    save_on_top = True


class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name')
    list_editable = ('is_active',)
    search_fields = ('name',)


admin.site.register(Habr, AdminHabr)
admin.site.register(Category, AdminCategory)

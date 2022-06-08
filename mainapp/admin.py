from django.contrib import admin
from .models import *


# "This is a class that inherits from the admin.ModelAdmin class, and
# it's used to customize the admin interface for the Habr model."
#
# The list_display attribute is used to specify which fields are displayed on the change list page for the object
class AdminHabr(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_active', 'is_ask_published', 'is_published', 'category',
                    'habr_view', 'tags')
    list_display_links = ('id', 'title')
    list_editable = ('is_active', 'is_ask_published', 'is_published', 'category', 'tags')
    search_fields = ('title', 'content', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('time_create', 'time_update', 'title', 'slug', 'category', 'content', 'user', 'is_active',
              'is_ask_published', 'is_published', 'likes', 'tags',)
    readonly_fields = ('time_create', 'time_update')
    save_on_top = True

    def get_form(self, request, obj=None, **kwargs):
        """
        It returns a form object that has a custom widget for the tags field, and sets the tags and likes fields to be
        optional

        :param request: The current request object
        :param obj: The object being edited
        :return: The form is being returned.
        """
        form = super(AdminHabr, self).get_form(request, obj, **kwargs)
        form.base_fields['tags'].widget.attrs['style'] = 'width: 80%;'
        form.base_fields['tags'].required = False
        form.base_fields['likes'].required = False
        return form

class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name')
    list_editable = ('is_active',)
    search_fields = ('name',)


admin.site.register(Habr, AdminHabr)
admin.site.register(Category, AdminCategory)

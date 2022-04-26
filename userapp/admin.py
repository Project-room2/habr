from django.contrib import admin
from .models import User, UserProfile


admin.site.register(User)

admin.site.register(UserProfile)

# from .models import Category, Post, Comments, Like
#
#
# class PostAdmin(admin.ModelAdmin):
#     """переопределение модели Post, отображающейся в административной панели"""
#
#     prepopulated_fields = {'slug': ('name',)}
#     list_display = ('name', 'slug', 'is_active')
#     list_filter = ('is_active',)
#     search_fields = ('name', 'category__name')
#
#
# admin.site.register(Category, PostAdmin)
# admin.site.register(Post, PostAdmin)
#
#
# class CommentAdmin(admin.ModelAdmin):
#     """переопределение модели Comments, отображающейся в административной панели"""
#
#     list_display = ('user', 'post', 'created')
#     search_fields = ('text',)
#
#
# admin.site.register(Comments, CommentAdmin)
#
#
# class BlogLikeAdmin(admin.ModelAdmin):
#     """переопределение модели Like, отображающейся в административной панели"""
#
#     autocomplete_fields = ('liked_by', 'blog_post')
#     list_display = ('blog_post', 'liked_by', 'like', 'created')

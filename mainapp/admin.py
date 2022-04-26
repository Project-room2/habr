from django.contrib import admin
from .models import Category, Habr, HabrLike


admin.site.register(Habr)
admin.site.register(HabrLike)
admin.site.register(Category)

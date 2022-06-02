from django.test import TestCase
from django.template.defaultfilters import slugify
from mainapp.models import Habr, Category


# class ModelsTestCase(TestCase):
#     def test_post_has_slug(self):
#         """Posts are given slugs correctly when saving"""
#         post = Habr.objects.create(title="Это мой мервый Habr")
#
#         post.save()
#         self.assertEqual(Habr.slug, slugify(Habr.title))


class ModelsTestCase(TestCase):
    def test_category_has_slug(self):
        category = Category.objects.create(name="Тестовая категория")pip install pytest
        category.save()
        self.assertEqual(Category.slug, slugify(Category.name))
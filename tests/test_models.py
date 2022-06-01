from django.test import TestCase
from django.template.defaultfilters import slugify
from mainapp.models import Habr


class ModelsTestCase(TestCase):
    def test_post_has_slug(self):
        """Posts are given slugs correctly when saving"""
        post = Habr.objects.create(title="Это мой мервый Habr")

        post.author = "Иван Ивашкин"
        post.category = 'design'
        post.save()
        self.assertEqual(Habr.slug, slugify(Habr.title))
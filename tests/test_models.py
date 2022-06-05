from django.test import TestCase
from pytils.translit import slugify
from mainapp.models import Category, Habr
from userapp.models import User


class CreateHabrTestCase(TestCase):

    def setUp(self):
        self.cat1 = Category.objects.create(name = "TestCategory1", slug = slugify("TestCategory1"))
        self.cat2 = Category.objects.create(name = "TestCategory2", slug = slugify("TestCategory2"))
        self.user = User.objects.create(username = "testuser", is_staff = True, is_superuser = False,
                                        email = "test@test.com")

    def test_create(self):
        habr1 = Habr.objects.create(title = "Created by CreateHabrTestCase test № 1", content = "any",
                                    category_id = self.cat1.id, user = self.user,
                                    slug = slugify("Created by CreateHabrTestCase test № 1"))
        habr2 = Habr.objects.create(title = "Created by CreateHabrTestCase test № 2", content = "any",
                                    category_id = self.cat2.id, user = self.user,
                                    slug = slugify("Created by CreateHabrTestCase test № 2"))
        cnt = len(Habr.objects.all().filter(title__contains = 'Created by CreateHabrTestCase test №'))
        self.assertEqual(2, cnt, 'Habr records creating has failed!')

# Generated by Django 4.0.4 on 2022-05-03 13:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='активна')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Habr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название статьи')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст статьи')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('like_quantity', models.PositiveIntegerField(default=0, verbose_name='кол-во')),
            ],
            options={
                'verbose_name': 'Хабр',
                'verbose_name_plural': 'Хабры',
                'ordering': ('-time_create', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='активна')),
            ],
            options={
                'verbose_name': 'лайк',
                'verbose_name_plural': 'лайки',
            },
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_habr_habr_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habr',
            name='habr_view',
            field=models.IntegerField(default=0, verbose_name='просмотров'),
        ),
    ]
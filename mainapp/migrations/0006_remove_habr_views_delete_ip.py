# Generated by Django 4.0.4 on 2022-05-03 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_habr_habr_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habr',
            name='views',
        ),
        migrations.DeleteModel(
            name='Ip',
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-19 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201016_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_user',
        ),
    ]

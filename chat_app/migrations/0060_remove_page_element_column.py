# Generated by Django 3.1 on 2021-02-24 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0059_page_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page_element',
            name='column',
        ),
    ]

# Generated by Django 3.1 on 2021-02-12 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0047_table_data_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table_data',
            old_name='link',
            new_name='url',
        ),
    ]

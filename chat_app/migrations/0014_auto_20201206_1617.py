# Generated by Django 3.1 on 2020-12-06 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0013_auto_20201205_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heading_1',
            name='heading_text',
            field=models.CharField(blank=True, max_length=85, null=True),
        ),
    ]

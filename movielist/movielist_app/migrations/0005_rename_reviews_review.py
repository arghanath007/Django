# Generated by Django 4.0.3 on 2022-06-01 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movielist_app', '0004_reviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]

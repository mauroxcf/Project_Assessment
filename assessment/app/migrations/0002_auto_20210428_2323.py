# Generated by Django 3.2 on 2021-04-28 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='payments',
            new_name='payment',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]

# Generated by Django 3.2.10 on 2021-12-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_customeradress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeradress',
            name='owner',
        ),
        migrations.AddField(
            model_name='customeradress',
            name='owner',
            field=models.ManyToManyField(to='profiles.Customer'),
        ),
    ]
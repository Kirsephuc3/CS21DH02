# Generated by Django 4.2.6 on 2023-10-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coures', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='update_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='update_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
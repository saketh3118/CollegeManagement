# Generated by Django 4.1.7 on 2023-03-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_logindetails_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindetails',
            name='dept',
            field=models.CharField(default='department', max_length=30),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-15 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_materials_alter_mid1_data_structures_cse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindetails',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

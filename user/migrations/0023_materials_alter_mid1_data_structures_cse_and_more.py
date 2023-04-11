# Generated by Django 4.1.7 on 2023-04-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_mid1_data_structures_cse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='mid1',
            name='Data_Structures_Cse',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='mid1',
            name='Java_Programming_Cse',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='mid1',
            name='Web_Technologies_Cse',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='mid2',
            name='Data_Structures_Cse',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='mid2',
            name='Java_Programming_Cse',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='mid2',
            name='Web_Technologies_Cse',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_alter_mid1_name_alter_mid2_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mid2',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]

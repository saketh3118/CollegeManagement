# Generated by Django 4.1.7 on 2023-05-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_alter_semester_c1_alter_semester_c10_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='TotalCredits1',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='TotalCredits2',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='TotalCredits3',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='TotalCredits4',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='id',
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Day',
            field=models.CharField(default='sunday', max_length=20, primary_key=True, serialize=False),
        ),
    ]
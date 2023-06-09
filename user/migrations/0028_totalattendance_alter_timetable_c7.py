# Generated by Django 4.1.7 on 2023-05-22 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_remove_semester_totalcredits1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalAttendance',
            fields=[
                ('Dept', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('DM_TOTAL', models.IntegerField(default=0)),
                ('CNS_TOTAL', models.IntegerField(default=0)),
                ('EEA_TOTAL', models.IntegerField(default=0)),
                ('GB_TOTAL', models.IntegerField(default=0)),
                ('CD_TOTAL', models.IntegerField(default=0)),
                ('QA_TOTAL', models.IntegerField(default=0)),
                ('DM_LAB_TOTAL', models.IntegerField(default=0)),
                ('CD_LAB_TOTAL', models.IntegerField(default=0)),
                ('ENG_LAB_TOTAL', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='timetable',
            name='C7',
            field=models.CharField(default='', max_length=20),
        ),
    ]

# Generated by Django 4.0 on 2022-01-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentresult',
            name='student_result_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]

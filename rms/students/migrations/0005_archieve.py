# Generated by Django 4.0 on 2022-01-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_studentresult_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archieve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archieve_id', models.CharField(max_length=255)),
                ('item_id', models.CharField(max_length=255)),
                ('row', models.CharField(max_length=255)),
                ('bay', models.CharField(max_length=255)),
                ('shelf', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
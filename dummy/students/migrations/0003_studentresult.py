# Generated by Django 4.0 on 2022-01-08 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('students', '0002_student_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('module_name', models.CharField(max_length=255)),
                ('mark', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=255)),
                ('gpe', models.CharField(max_length=255)),
                ('credits', models.CharField(max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_student', to='accounts.user')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]

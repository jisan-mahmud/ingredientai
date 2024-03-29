# Generated by Django 5.0.1 on 2024-02-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email address')),
                ('full_name', models.TextField(max_length=50)),
                ('country', models.TextField(max_length=40)),
                ('city', models.TextField(max_length=40)),
                ('address', models.TextField(max_length=150)),
                ('phone_number', models.TextField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

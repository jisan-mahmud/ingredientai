# Generated by Django 5.0.1 on 2024-02-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_customuser_github_customuser_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='github',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='linkedin',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

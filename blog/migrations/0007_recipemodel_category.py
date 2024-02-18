# Generated by Django 5.0.1 on 2024-02-14 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_recipemodel_create_at'),
        ('category', '0002_alter_category_options_alter_category_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipemodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='category.category'),
        ),
    ]
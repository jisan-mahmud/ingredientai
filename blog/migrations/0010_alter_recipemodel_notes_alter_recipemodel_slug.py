# Generated by Django 5.0.1 on 2024-02-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_recipemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='notes',
            field=models.TextField(blank=True, default='This recipe is AI-generated and IngredientAI has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated dishes.'),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=300),
        ),
    ]
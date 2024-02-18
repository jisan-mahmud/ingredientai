from django.contrib import admin
from .models import RecipeModel
# Register your models here.

class RecipeModelAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ['recipe_name']}
    list_display = ['recipe_name']

admin.site.register(RecipeModel, RecipeModelAdmin)
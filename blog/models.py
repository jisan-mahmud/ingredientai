from django.db import models
from category.models import Category
from accounts.models import CustomUser
# Create your models here.

#recipe_name, cooking_time, calorie, ingredients, instructions,notes
class RecipeModel(models.Model):
    recipe_name = models.CharField(max_length= 250)
    slug = models.SlugField(max_length= 300, blank= True, null= True)
    image = models.ImageField(upload_to= 'recipe_image/', blank= True, default= 'recipe_image/recipe_thumb.webp')
    about = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE, default= 1)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name= 'recipe')
    cooking_time = models.CharField(max_length= 50)
    calorie = models.CharField(max_length= 20)
    ingredients = models.TextField()
    instructions = models.TextField()
    notes = models.CharField(max_length= 250, blank= True, default= 'This recipe is AI-generated and IngredientAI has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated dishes.')
    create_at = models.DateTimeField(auto_now_add= True)
    views = models.IntegerField(blank= True, default= 0)
    def __str__(self):
        return self.recipe_name

    class Meta:
        verbose_name = 'Recipe'

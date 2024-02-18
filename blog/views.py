from django.shortcuts import render
from django.views import View
from .models import RecipeModel
from category.models import Category
from django.core.paginator import Paginator
# Create your views here.

class RecipeView(View):
    #this id recipe category id
    def get(self, request, id= None):
        categories = Category.objects.all()
        if id is not None:
            recipes = RecipeModel.objects.filter(category__id= id).order_by('-create_at')
        else:
            recipes = RecipeModel.objects.all().order_by('-create_at')

        #generate paginations
        paginator = Paginator(recipes, 8)
        page_number = request.GET.get('page')
        recipes_obj = paginator.get_page(page_number)
        return render(request, 'blog/blog.html', {'recipes': recipes_obj, 'categories': categories})

class RecipeDetailsView(View):
    def get(self, request, id, slug):
        recipe_object = RecipeModel.objects.get(id= id, slug= slug)
        context = {
            'ingredients': eval(recipe_object.ingredients),
            'instructions': eval(recipe_object.instructions),
            'recipe_object': recipe_object
        }
        #increment view
        recipe_object.views += 1
        recipe_object.save()
        return render(request, 'blog/recipe-details.html', context)
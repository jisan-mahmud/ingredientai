from django.shortcuts import render, redirect
from django.views import View
from blog.models import RecipeModel
from .generate import generate_recipe
from category.models import Category
from .slug_generate import slug
from django.contrib import messages
# Create your views here.

class GenerateView(View):
    def get(self, request):
        return render(request, 'generate/generate.html')


#Tsis view for making recipe with image
def generatewithimage(request):
    if request.method ==  'POST':
        if 'image' in request.FILES:
            image = request.FILES.get('image')
            try:
                #get all category
                categorys = Category.objects.all()
                #concate all category in a string
                category_str = ''
                for category in categorys:
                    category_str += (category.category_name + ', ')

                #generate recipe for this image
                generated_recipe = generate_recipe(img= image, category= category_str)

                #find category for this recipe
                category_id = Category.objects.filter(category_name= generated_recipe.get('category_name'))[0]
                #create a recipe blog
                recipe_object = RecipeModel.objects.create(
                    user= request.user,
                    recipe_name= generated_recipe.get('recipe_name'),
                    slug= slug(generated_recipe.get('recipe_name')),
                    about= generated_recipe.get('about'),
                    category=  category_id,
                    image= image,
                    cooking_time= generated_recipe.get('cooking_time'),
                    calorie= generated_recipe.get('calorie'),
                    ingredients= generated_recipe.get('ingredients'),
                    instructions= generated_recipe.get('instructions'),
                    )
                recipe_object.save()
                return redirect('recipe_details', recipe_object.id, recipe_object.slug)
            except Exception as e:
                messages.error(request, 'Something is wrong! Try again later.')
        else:
            messages.error('Image not found! Try again later.')

    return redirect('generate')

#This view for making recipe with custom instruction
class GenerateRecipeWithInstruction(View):
    def post(self, request):
        protein = request.POST.get('protein')
        nutritional = request.POST.get('nutritional')
        cuisine = request.POST.get('cuisine')

        try:
            #get all category
            categorys = Category.objects.all()
            #concate all category in a string
            category_str = ''
            for category in categorys:
                category_str += (category.category_name + ', ')

            instruction = f'protein: {protein}, nutritional: {nutritional}, cuisine: {cuisine}'
            #generate recipe for this image
            generated_recipe = generate_recipe(ingredients= instruction, category= category_str)

            # #find category for this recipe
            category_id = Category.objects.filter(category_name= generated_recipe.get('category_name'))[0]
            #create a recipe blog
            recipe_object = RecipeModel.objects.create(
                user= request.user,
                recipe_name= generated_recipe.get('recipe_name'),
                slug= slug(generated_recipe.get('recipe_name')),
                about= generated_recipe.get('about'),
                category=  category_id,
                cooking_time= generated_recipe.get('cooking_time'),
                calorie= generated_recipe.get('calorie'),
                ingredients= generated_recipe.get('ingredients'),
                instructions= generated_recipe.get('instructions'),
                )
            recipe_object.save()
            return redirect('recipe_details', recipe_object.id, recipe_object.slug)
        except Exception as e:
            messages.error(request, 'Something is wrong! Try again later.')
        return redirect('generate')
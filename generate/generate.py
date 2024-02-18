import google.generativeai as genai
import json
from PIL import Image
API_KEY = 'AIzaSyCm7UcDfolvxk_JWWr-Q9cdYSbsp5zs2-A'

def generate_recipe(category, ingredients= None, img= None):
    genai.configure(api_key= API_KEY)
    system_istruction = 'Give this recipe in python dictionary: {recipe_name, category_name, about, cooking_time, calorie, ingredients, instructions} keys.Dictionary name: "recipe".Do not use subdictionary and "ingredients, instructions" store in python list always follow this one formate.' + f'Add category_name for this recipe in recipe key dictionary from {category} this string.'

    try:
        if ingredients is not None and img is None:
            instruction = ingredients + 'make a recipe with this instructions. ' + system_istruction
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(instruction)
        elif ingredients is None and img is not None:
            try:
                img = Image.open(img)
            except Exception as image_error:
                return image_error
            instruction = 'Extract food ingredients from this image and make a recipe. ' + system_istruction
            model = genai.GenerativeModel('gemini-pro-vision')
            response = model.generate_content([instruction, img])
        else:
            return ValueError('Either ingredients or img should be provided.')

        if response is not None:
            #response text split with =. and convert into json file for parse data
            response_str = json.loads(response.text.split('=')[1][0:-3])
            # parse all data
            recipe_name = response_str['recipe_name']
            about = response_str['about']
            category_name = response_str['category_name']
            cooking_time = response_str['cooking_time']
            calorie = response_str['calorie']
            ingredients = response_str['ingredients']
            instructions = response_str['instructions']
            return {'recipe_name': recipe_name, 'about': about, 'category_name':category_name, 'cooking_time': cooking_time, 'calorie': calorie, 'ingredients': ingredients, 'instructions': instructions,}
        else:
            raise ValueError('Something is wrong. Try again!')
    except Exception as error:
        return error

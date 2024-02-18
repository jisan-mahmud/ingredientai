from django.urls import path
from .views import RecipeDetailsView, RecipeView
urlpatterns = [
    path('recipes/', RecipeView.as_view(), name= 'recipes'),
    #this id is category id
    path('recipes/<int:id>', RecipeView.as_view(), name= 'recipes'),
    path('recipe/<int:id>/<slug>', RecipeDetailsView.as_view(), name='recipe_details')
]

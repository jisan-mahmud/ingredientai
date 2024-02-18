from django.urls import path
from .views import GenerateView, generatewithimage, GenerateRecipeWithInstruction
urlpatterns = [
    path('', GenerateView.as_view(), name='generate'),
    path('using-image/', generatewithimage, name='using_image'),
    path('using-instruction/', GenerateRecipeWithInstruction.as_view(), name='using_instruction')

]

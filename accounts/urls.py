from django.urls import path
from .views import signup, activate, MyRecipe, edit_profile, change_password, user_login, user_logout, ProfileVisit, ResetPassword
urlpatterns = [
    path('sign-up', signup, name='sign_up'),
    path('activate<uidb64>/<token>', activate, name='activate'),
    path('my-recipe/', MyRecipe.as_view(), name= 'my_recipe'),
    path('profile', edit_profile, name='profile'),
    path('change-password', change_password, name= 'change_password'),
    path('sign-in', user_login, name='sign_in'),
    path('logout/', user_logout, name='logout'),
    path('reset-password/', ResetPassword.as_view(), name='rest_password'),
    path('profile-visit/<int:id>', ProfileVisit.as_view(), name='views_profile')
]

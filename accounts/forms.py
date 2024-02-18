from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

class CreateUser(forms.ModelForm):
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password', 'password2']

    def clean(self):
        clean_data = super().clean()
        password1 = clean_data.get('password')
        password2 = clean_data.get('password2')


        # Check if passwords match
        if password1 != password2:
            raise ValidationError("Passwords don't match.")

        # Check additional password complexity rules
        if password1:
            # Add your own password complexity rules here
            if len(password1) < 8:
                raise ValidationError("Password must be at least 8 characters long.")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['profile_photo', 'full_name', 'country', 'city', 'address', 'phone_number', 'date_of_birth', 'github', 'twitter', 'linkedin', 'bio']

class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
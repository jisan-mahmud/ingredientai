from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name= 'email address', max_length= 100, unique= True)
    profile_photo = models.ImageField(upload_to= 'profile_photos/', blank= True, default='profile_photos/profile.jpg')
    full_name = models.CharField(max_length= 50)
    bio = models.CharField(max_length= 100, default= '', blank= True)
    country = models.CharField(max_length= 40, blank= True)
    city = models.CharField(max_length= 40, blank= True)
    address = models.CharField(max_length= 150, blank= True)
    phone_number = models.CharField(max_length= 15, blank= True)
    date_of_birth = models.DateField(blank= True, null= True)
    twitter = models.CharField(max_length= 100, blank= True)
    github = models.CharField(max_length= 100, blank= True)
    linkedin = models.CharField(max_length= 100, blank= True)

    is_active = models.BooleanField(default= False)
    is_staff = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default= False)
    date_joined = models.DateTimeField(default= timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

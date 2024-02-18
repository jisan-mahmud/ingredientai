from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length= 100, unique= True)
    slug = models.SlugField(max_length= 150, blank= True, null= True)

    class Meta:
        verbose_name= 'category'
        verbose_name_plural= 'categories'
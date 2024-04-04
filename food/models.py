from django.db import models


from django.urls import reverse

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length = 250 , unique=True)

    class Meta:

        verbose_name_plural = 'categories'
    
    def __str__(self):

        return self.name
    
    def get_absolute_url(self):

        return reverse('list-category', args=[self.slug])    


class Product(models.Model):

    # FK
    Category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length= 250)

    slug = models.SlugField(max_length=250, unique=True)

    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField(help_text='Preparation time in minutes')

    image = models.ImageField(upload_to='imagees/')

    class Meta:

        verbose_name_plural = 'Products'
    
    def __str__(self):

        return self.title
    
    def get_absolute_url(self):

        return reverse('product-details', args=[self.slug])



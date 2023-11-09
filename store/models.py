from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class Location(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Item(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE )
    quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=50)
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Allocation(models.Model):
    category = models.ForeignKey(Category, related_name='allocation', on_delete=models.CASCADE )
    location = models.ForeignKey(Location, related_name='allocation', on_delete=models.CASCADE )
    quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=50)
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.title

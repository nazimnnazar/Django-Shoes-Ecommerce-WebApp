from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to='product')
    caetgory = models.ForeignKey(Category,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name
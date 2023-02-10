from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField(null=True,blank=True)
    photo = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    text = models.TextField()
    

    def __str__(self):
        return self.name

class Shop(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE,related_name='shop_client')
    date =models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    def __str__(self):
        return str(self.client)
    
   
    

class ShopItems(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='item_savatcha')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='item_product')
    quantity = models.IntegerField()
    totalPay = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)    

class BlogPage(models.Model):
    photo = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=200)
    text1 = models.TextField()
    text2 = models.TextField()

    def str(self):
        return self.name

class PhotoMain(models.Model):
    photo1 = models.ImageField(upload_to='media/')
    photo2 = models.ImageField(upload_to='media/')
    photo3 = models.ImageField(upload_to='media/')
    photo4 = models.ImageField(upload_to='media/')
    photo5 = models.ImageField(upload_to='media/')

    
    def str(self):
        return str(self.id)

class PhotoCarucel(models.Model):
    photo = models.ImageField(upload_to='media/')

    def str(self):
        return str(self.id)

class Xarita(models.Model):
    joy = models.CharField(max_length=500)

    def str(self):
        return str(self.joy)

    


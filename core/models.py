from django.db import models
from django.contrib.auth.models import User
import datetime
from django_ckeditor_5.fields import CKEditor5Field
import uuid
# Create your models here.
class Featured(models.Model):
    bio = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='featured-images')
    
    def __str__(self):
        return f'{self.title}'
    
class MyService(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    icon = models.CharField(max_length=50) 
    
    def __str__(self):
        return f'{self.name}'
    
    
class Post(models.Model):
    
    STATUS =(
        ('DRAFT', 'DRAFT'),
        ('PUBLISH','PUBLISH')
    )
    img = models.ImageField(upload_to='blog_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    body = CKEditor5Field('Text', config_name='extends')
    status = models.CharField(choices=STATUS, default='DRAFT', max_length=100)
    
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    
# class Faq(models.Model):
#     faqid = models.UUIDField(primary_key=True,auto_created=True)
#     question = models.CharField(max_length=256)
#     answer1 = models.CharField(max_length=256,blank=True)
#     answer2 = models.CharField(max_length=256, blank=True)
#     answer3 = models.CharField(max_length=256, blank=True)
#     answer4 = models.CharField(max_length=256,blank=True)
#     answer5 = models.CharField(max_length=256, blank=True)
    
#     def __str__(self):
#         return f'{self.question}'
    
    
class Faq_image(models.Model):
    img1 = models.ImageField(upload_to='faq_img')
    img2 = models.ImageField(upload_to='faq_img')
    
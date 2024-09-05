from django.db import models
from django.contrib.auth.models import User



class Book(models.Model):
    user= models.ForeignKey(User,on_delete=models.SET_NULL, null= True, blank= True)
    book_name=models.CharField(max_length=250)
    book_description=models.TextField()
    book_image=models.ImageField( upload_to='bookimages', height_field=None, width_field=None)
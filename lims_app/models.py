from django.db import models

class book(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description=models.CharField(max_length=1000,default="Description")
    is_available=models.BooleanField(default=True)
    def __str__(self):
        return self.title
    

class Users(models.Model):
    name=models.CharField(max_length=50)
    is_reading=models.BooleanField(default=False)
    book_reading=models.ForeignKey(book,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name
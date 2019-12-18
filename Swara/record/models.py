from django.db import models
from django.conf import settings

# Create your models here.
class Word(models.Model):
    name = models.CharField(max_length=10)

    
    def __str__(self):
        return self.name
    


class Entry(models.Model):
    title = models.ForeignKey(Word, default=1, on_delete=models.SET_DEFAULT)
    date = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to = 'media/', null=True)


    def __str__(self):
        return self.title.name 
    

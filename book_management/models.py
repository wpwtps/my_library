from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
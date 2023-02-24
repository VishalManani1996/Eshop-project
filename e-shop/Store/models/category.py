from django.db import models

class Category(models.Model):
 name=models.CharField(max_length=20)

 @staticmethod
 def get_all_categories():
    return Category.objects.all()

 def __str__(self):         #Shows actual name instead of category.object
     return self.name
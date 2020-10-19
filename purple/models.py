from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length = 200)	
    item_desc = models.CharField(max_length = 200)
    item_image = models.CharField(max_length = 500,default = 'https://image.shutterstock.com/image-illustration/colourful-business-logo-company-name-260nw-1779060338.jpg')


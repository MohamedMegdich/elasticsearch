from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(null=True,blank=True,max_length=120)
    timestamp = models.DateTimeField(auto_now_add=False)
    publish = models.DateTimeField(auto_now_add=False,null=True)


    def get_absolute_url(self):
        return f'products/{self.id}'

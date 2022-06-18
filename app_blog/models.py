from django.db import models 

# Create your models here.
class product(models.Model):
    product_type = models.CharField(max_length=30, null= True)
    product_name = models.CharField(max_length=30,null=True)
    descr = models.TextField(null=True)
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to = 'prodimg')

    def __str__(self) -> str:
        return self.product_name

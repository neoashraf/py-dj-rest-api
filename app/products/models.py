from django.db import models

# Create your models here.
class Product(models.Model):
    title             = models.CharField(max_length = 20)
    description       = models.TextField(blank=True, null=True)
    price             = models.DecimalField(decimal_places=2, max_digits=100)
    summary           = models.TextField()
    featuredId        = models.BooleanField()
    rating            = models.DecimalField(decimal_places=2, max_digits=3,null=True)
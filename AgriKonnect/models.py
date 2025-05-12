from django.db import models

# Create your models here.

class Plot(models.Model):

    size_in_hectares= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    suitable_crops = models.CharField(max_length=100)
    estimate_of_harvest_yield = models.CharField(max_length=100)
    for_rent = models.BooleanField(default=True)
    for_sale = models.BooleanField(default=False)
    sale_price = models.CharField(max_length=100)
    rent_price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures')
    name_of_owner = models.CharField(max_length=100)
    owner_contact = models.CharField(max_length=100)

from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    msrp = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    purchase_link = models.CharField(max_length=300)
    description = models.CharField(max_length=400)


    def __str__(self):
        return self.name

class Collection(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name='collections')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
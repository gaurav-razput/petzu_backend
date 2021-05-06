from django.db import models


class Pet(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.TextField()
    breedName = models.TextField()
    description = models.TextField()
    age = models.IntegerField()
    gender = models.TextField()
    color = models.TextField()
    weight = models.IntegerField()
    height = models.IntegerField()
    length = models.IntegerField()
    sellerId = models.IntegerField()
    sellerName = models.TextField()
    longDescription = models.TextField()
    breedId = models.IntegerField()

    class meta:
        ordering = ['created']

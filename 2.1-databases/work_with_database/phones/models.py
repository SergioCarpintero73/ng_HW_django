from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.TextField()
    lte_exists = models.TextField()
    slug = models.TextField()

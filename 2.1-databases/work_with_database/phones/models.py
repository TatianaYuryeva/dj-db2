from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    # price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    # release_date = models.DateField(default='2000-01-01')
    release_date = models.CharField(max_length=50)
    lte_exists = models.BooleanField()
    slug = models.SlugField()

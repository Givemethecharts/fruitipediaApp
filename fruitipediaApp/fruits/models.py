from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from fruitipediaApp.fruits.validators import fruit_name_only_letters


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False, null=False)


class Fruit(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, validators=[MaxLengthValidator(30), MinLengthValidator(2), fruit_name_only_letters])

    Image_url = models.URLField(blank=False, null=False)

    description = models.TextField(blank=False, null=False)

    nutrition = models.TextField(blank=True, null=True)


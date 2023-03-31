from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

from storehouse.models import Ingredient


class DishType(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    class Meta:
        ordering = ["username"]


class Dish(models.Model):
    name = models.CharField(max_length=63, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    dish_type = models.ForeignKey(DishType,
                                  on_delete=models.SET_NULL, null=True,)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient,
                                         related_name="dishes", default=None)

    class Meta:
        ordering = ["name"]
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self):
        return self.name

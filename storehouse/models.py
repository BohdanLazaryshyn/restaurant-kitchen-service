from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=63)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit = models.CharField(max_length=63, default="g")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

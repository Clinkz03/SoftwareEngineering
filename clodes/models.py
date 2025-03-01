from django.db import models

# Create your models here.
class MyClothes(models.Model):
    CATEGORY_CHOICES = [
        ('T', 'Top'),
        ('B', 'Bottom'),
        ('O', 'Outerwear'),
        ('F', 'Footwear'),
        ('A', 'Accessory'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    colour = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    material = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

from django.db import models

# Create your models here.

class Book(models.Model):
    CATEGORY_CHOICES = (
        ('FI', "fiction"),
        ('NF', "non-fiction"),
    )

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    is_available = models.BooleanField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        null=True,
    )

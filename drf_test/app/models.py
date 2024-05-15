from django.db import models


class Products(models.Model):
    # Product Model
    title = models.CharField(max_length=255)
    asin = models.CharField(max_length=30, unique=True)

    def __str__(self) -> models.CharField:
        return self.asin


class Reviews(models.Model):
    # Review Model
    asin = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    title = models.CharField(max_length=255, blank=True)
    review = models.TextField()

    def __str__(self) -> models.CharField:
        return self.title

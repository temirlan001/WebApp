from django.db import models


# Create your models here.
class BrandData(models.Model):
    brand = models.CharField(max_length=100)
    rise = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Brand Population Data'

    def __str__(self):
        return f'{self.brand}-{self.rise}'


class CsvData(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    price = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'notebooks'

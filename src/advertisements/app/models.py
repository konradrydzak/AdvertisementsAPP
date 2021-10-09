from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    ordering = models.PositiveIntegerField()

    class Meta:
        db_table = 'category'


class Offer(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=999, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')

    class Meta:
        db_table = 'offer'

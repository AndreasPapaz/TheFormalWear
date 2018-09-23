from django.db import models

class Product(models.Model):
    name = models.CharFields(max_length=30)
    type = models.CharFields(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

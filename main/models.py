from django.db import models

# Create your models here.
import uuid

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('forward', 'Forward'),
        ('midfield', 'Midfield'),
        ('centerback', 'Centerback'),
        ('fullback', 'Fullback'),
        ('goalkeeper', 'Goalkeeper'),
        ('manager', 'Manager'),
        ('exclusive', 'Exclusive'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    price = models.IntegerField(null=True, blank=True, default=0)
    category = models.CharField(choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.title
    


        

from django.db import models

# Create your models here.

class URLMappings(models.Model):
    auto_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=500)
    mapping_url = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)



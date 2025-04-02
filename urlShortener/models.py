from django.db import models

class ShortUrl(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.short_code} -> {self.url}"
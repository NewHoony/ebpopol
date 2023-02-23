from django.db import models

class Tech(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='wtech/pdfs/')
    cover = models.ImageField(upload_to='wtech/covers/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Book(models.Model):
    site_name = models.CharField(max_length=100, null=True, blank=True)
    site_url = models.TextField()
    site_con = models.TextField(max_length=200)
    site_cover = models.ImageField(upload_to='wtech/bookcovers/', null=True, blank=True)

    def __str__(self):
        return self.site_name
# Create your models here.

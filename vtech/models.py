from django.db import models

class Tech(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='vtech/pdfs/')
    cover = models.ImageField(upload_to='vtech/covers/', null=True, blank=True)

    def __str__(self):
        return self.title
# Create your models here.

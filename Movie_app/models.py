from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    release_date = models.DateField(null=True)
    runtime = models.IntegerField(help_text="Runtime in minutes",default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.FileField(default=0,upload_to='movie_images')
    

    def __str__(self):
        return self.title

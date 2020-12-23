from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=80)
    create_date = models.DateField(auto_now_add=True)
    information = models.TextField(blank=True)
    image_url = models.CharField(max_length=255,blank=True)
    url = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.title , self.create_date

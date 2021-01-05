from django.db import models

class bookModel(models.Model):
    title = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 50, blank = True, null = True)
    img = models.ImageField(upload_to = "media")


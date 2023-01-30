from django.db import models

class File(models.Model):

    file = models.TextField(unique=True)
    list_of_word = models.TextField()

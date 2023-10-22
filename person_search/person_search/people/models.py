from django.db import models

class Person(models.Model):
    unique_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        app_label = 'people'

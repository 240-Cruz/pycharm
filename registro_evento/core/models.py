from django.db import models

class register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    num_doc = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date = models.DateField()
    coments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name +"-" + self.last_name



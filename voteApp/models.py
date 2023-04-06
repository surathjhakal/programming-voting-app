from django.db import models
# Create your models here.


class MySiteUser(models.Model):
    name = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"Name: {self.name} Email: {self.email}"
    

class CreateProgrammingLanguage(models.Model):
    name = models.CharField(max_length=64)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Name: {self.name} Count: {self.count}"
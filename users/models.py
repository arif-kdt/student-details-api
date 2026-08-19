from django.db import models

class Student(models.Model):
    rollNo = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
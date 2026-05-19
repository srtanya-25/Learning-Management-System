from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id= models.IntegerField()
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=100)
    def __str__(self):
        return f"{self.teacher_id} . {self.name} - {self.email}"
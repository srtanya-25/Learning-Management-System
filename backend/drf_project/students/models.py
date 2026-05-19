from django.db import models
from mentors.models import Mentor

# Create your models here.
class Student(models.Model):
    student_id= models.IntegerField(primary_key=True) #ts wil create primary key directly, that is the student_id field
    name=models.CharField(max_length=25)
    branch= models.CharField(max_length=25)
    email=models.EmailField(max_length=100)
    mentor= models.ForeignKey(Mentor, on_delete=models.SET_NULL, null= True, related_name="students")
   

    def __str__(self):
        return f"{self.student_id} . {self.name} - {self.email} : {self.mentor}"
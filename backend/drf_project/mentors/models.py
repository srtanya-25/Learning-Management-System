from django.db import models

# Create your models here.
class Mentor(models.Model):
    mentor_id=models.CharField(max_length=25, primary_key=True, default='General')
    mentor_name= models.CharField(max_length=25, default='General')
    mentor_email= models.EmailField(default='General')
    mentor_expertise= models.CharField(max_length= 100, null=True, blank=True) #to not let migrations fail
    #nested serializer to get students in the mentor api page, so we r changing in mentor serializer


    def __str__(self):
        return f"{self.mentor_name}" 

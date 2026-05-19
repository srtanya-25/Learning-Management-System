from rest_framework import serializers
from teachers.models import Teacher
from students.models import Student
from mentors.models import Mentor
from mentors.serializers import Mentor_Serializer

class TeacherSerializer(serializers.ModelSerializer):
    class Meta: #inner class
        model = Teacher #serilizer for teacher model so that the quessryset data converts into json format without the manual list conversion
        fields="__all__" #dunder all brings all the fields from the teacher model

class StudentSerializer(serializers.ModelSerializer):
    mentor = serializers.SlugRelatedField(slug_field='mentor_name', queryset= Mentor.objects.all()) #this field name shld be same as in the Student model, read_only+true is for not allowing any edition of mentor name,, for getting only one primary key as its j post creating a new object
    #mentor = Mentor_Serializer(read_only=True) # for getting whole details of the mentor , its j reading
    #slug relatedfield changes the relation to the field of our choice
    class Meta: #inner class 
        model = Student #serilizer for student model so that the quessryset data converts into json format without the manual list conversion
        fields="__all__"
        #fields=['student_id','name','email','mentor'] 

class MentorSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True) #to get a student field so we add inside mentorserializer, same name in relted_name of student model
    class Meta: #inner class
        model = Mentor #serilizer for student model so that the quessryset data converts into json format without the manual list conversion
        fields=['mentor_id','mentor_name','mentor_email','mentor_expertise','students'] #can change the seqeunce of the fields
        #serializer is contrilling the order of fields
        
#request of all students details
'''PAGINATION: two types
page no pagination: i want each page how many records
limit offset: '''
'''implementation: 
global pagination: for all api, files ts pagination is applied
custom pagination: per page
/students/?limit=20 & offset=10
limit the adding page no, offset from where to start +1 
eg: limit=20, offset= 10, (from 11 till 30)
offset+1 till offset+llimit
paze size: no of reocrds
0+1 pages
'''
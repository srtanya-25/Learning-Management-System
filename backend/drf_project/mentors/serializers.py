############

from rest_framework import serializers
from .models import Mentor


class Mentor_Serializer(serializers.ModelSerializer):
    #students = StudentSerializer(many=True) #to get a student field so we add inside mentorserializer, same name in relted_name of student model
    class Meta: #inner class
        model = Mentor #serilizer for student model so that the quessryset data converts into json format without the manual list conversion
        fields="__all__" #can change the seqeunce of the fields
        #serializer is contrilling the order of fields
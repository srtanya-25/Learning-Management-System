from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def teachers(request):
    teacher_data=[{'id':1,'name':'abc', 'email':'John@gmail'}]
    return HttpResponse(teacher_data)

#/api/v2
#this is the web endpoint
from django.urls import path
from . import views
urlpatterns=[
    path('',views.teachers,name='teachers_home')
]

    #slug: url friendly datatype

#no need tthe url of teachers too as all works with api itself
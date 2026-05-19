from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
from teachers.models import Teacher
from students.models import Student
from mentors.models import Mentor
#from students.serializers import StudentSerializer
from .serializers import TeacherSerializer
#from mentors.serializers import Mentor_Serializer
from .serializers import MentorSerializer
from .serializers import StudentSerializer
#why shldnt we do from .serializers import * (it causes problem in common function as if we have smae functsion name the below function name will be taken not the before one, so importing awll iis necseeary)
#we can create alias if same function name
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView #to any view class it make its api view function which will allow request
#from rest_framework.pagination import PageNumberPagination
from students.paginations import StudentPagination
from students.filters import StudentFilter
from mentors.filters import MentorFilter
from rest_framework.filters import SearchFilter #searching
from rest_framework.filters import OrderingFilter #sotring or orderinng
from django.contrib.auth.models import User
from  rest_framework.permissions import AllowAny

#normal view function now api view function enhanced by @ decorator for api
#decorators on a functon or method outisde or inside class
#put will send the data but it wont get into anything in middle of any other data it will send at the bottom.
# Create your views here.
@api_view(["GET","POST"]) #view to convert into api view hence get request needs to be allowed to teachers_api_view
def teachers_api_view(request): 
    
    if request.method=="GET":
        teachers= Teacher.objects.all() #query set
        serialized_data= TeacherSerializer(teachers,many=True) #serialized object, many=true for many data
        return Response(serialized_data.data, status=status.HTTP_200_OK) #status for 202 for success and something like ts, POST request, status shown to theclient who is hitting my api endpoint
    
    #return JsonResponse(teachers, safe=False)
    elif request.method == "POST":
        query_set = TeacherSerializer(data=request.data)
        if query_set.is_valid():
            query_set.save() #save the data into Db
            return Response(query_set.data, status=status.HTTP_201_CREATED) #data is sending back to the page if we dont have quesr.data it wont
        else:
            return Response(query_set.errors, status=status.HTTP_400_BAD_REQUEST) #errors will sent when its working
        
#Django creates an id which is primary key no duplicates and null
#update: put, delete: delete, - get,edit, delete
                
#serializertaion : quesry set into another list or xml format
#deserialization: its opposite of serialization
#this is api endpoint, we r the server not the client, we r cretaing api afor someone else, but when we use the api we r the client
@api_view(['GET','PUT','DELETE'])
def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk) #pk is another alias for id, isnated of id we can even put pk, which is alr id
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #we can put under the function , we can use get, put, delete
    if request.method == "GET":
        serialized_data= TeacherSerializer(teacher)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data=request.data
        serial = TeacherSerializer(teacher, data=data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status.HTTP_200_OK)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =="DELETE":
        teacher.delete()
        return Response("Successfully Deleted.",status=status.HTTP_204_NO_CONTENT)
    
    #POST creates a new object
    #http://127.0.0.1:8000/api/v1/teacher/1
    

    
# #Class based view
# class StudentsView(APIView): #works like a inheritance, APIView which we r iniheriting will do the task of the decorator
#     def get(self, request): #fro every request we will create an instance method
#         students= Student.objects.all()
#         serializer= StudentSerializer(students,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self,request):
#         data= request.data
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #if ay data is given wrong via client side
    
# class StudentDetail(APIView):
#     def get(self, request, pk): #every request is a method: get, put and all needs request
#         try: 
#             student=Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             serializer= StudentSerializer(student)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#     def put(self, request, pk): #every request is a method: get, put and all needs request
#         try: 
#             student=Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             serializer= StudentSerializer(student, data=request.data) #desiralizer
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_200_OK) #202 for accepted, but proecssing is not compelted hence 200 as in our case processing is completed
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             # foe web endpint we use/ blogs/ something like that
#             #but in api itss diff
#     def delete(self, request, pk): #every request is a method: get, put and all needs request
#         try: 
#             student=Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             student.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

'''we use mixins to create class based views: 5types 
inbuilt instances: ListModelMixins, CreateModelMixins, RetrieveModelMixins, UpdateModelMixins, DestroyModelMixins
ListModelMixins: GET
CreateModelMixins: POST 
RetrieveModelMixins: GET(pk) 
UpdateModelMixins: PUT(pk)
DestroyModelMixins: DELETE(pk)'''
'''GENERICS: before isntead of decorators we used instead of apiview to allow the request in students, 
but in second method we use in mixins is Generic.api( even does some formatting)'''

# GENERIC, MIXINS: built in modules
# MIXINS: sending resposne on our behlaf,does all the serializng part, we j  create a queryset data ,tell which is our serilizer and wheres the data, call get method
#GENERICS: api view

#below class for get, post method only 
'''class StudentsView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset= Student.objects.all() 
    #inbuilt attriute mixins which queryset, serializer_class shld be the same name only,
    #cannot be anything, internally to allow the query set to access the data
    #attribute created internally, to undertsnad query sate has the data
    #serializer_class= StudentSerializer

    def get(self, request):
        return self.list(request)  #coming from ListModelMixin
    def post(self, request):
        return self.create(request) #coming from CreateModelMixin

class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)
    def put(self, request, pk):
        return self.update(request, pk)
    def destroy(self, request, pk):
        return self.destroy(request, pk)'''
    
'''Generic gives onlyfew lines(works like encapsulation): functions will go away
Generic Inbuilt classes: 
api/v1/students
ListAPIView -> GET (All Data) (non primary key)
CreateAPIView -> POST
api/v1/student/1
RetrieveAPIView -> GET(pk)
UpdateAPIView -> PUT (pk)
DestroyAPIView -> DELETE (pk)'''
'''In Generic Inbuilt Classes we merge the steps of list and create into one i.e 
ListCreateAPIView -> GET & POST
generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView to one : RetrieveUpdateDestroy'''

'''#Generics Class based views 
class StudentsView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer'''

# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class= StudentSerializer
    #lookup_field='pk' #or lookup_field='student_id'

#Class based View Using View Sets
class StudentsView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    pagination_class= StudentPagination
    #filterset_fields = ['branch'] #ts is for global filter
    filterset_class = StudentFilter #for customfilter
    filter_backends = [OrderingFilter]
    ordering_fields = ['student_id', "name"]
    permission_classes = [AllowAny]


class MentorsView(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class= MentorSerializer
    filterset_class= MentorFilter
    filter_backends= [SearchFilter, OrderingFilter] #searchfilter is a inbuuilt class to search the records, it is a list
    search_fields= ["mentor_expertise"]
    ordering_fields = ['mentor_name']
    permission_classes = [AllowAny]

#serilizer and view is combined in ViewSets, it does the CRUD: create read update delete operations
#class viewset which has module view set
#modelview set: takes only query and serializers and provides both primary n non primary key operations
class MentorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class= MentorSerializer

'''REACT : Javascript library/framework helps us to built ui and components(reusuable block)
who created reacte: facebook wanted single page application
vitural dome(vdome) : instead of reloading the entire page, it j reoload speacifi component or part we hv updated which makes react faster'''
#greatfrontend.com: frontend questions
#react needs node.js is a runtime framwork , hence required firtly to start reacat
#npm --version using ts we can install node packeges
#to install recta we use npx odler versoin and vite newer

'''django
djnagorestframework
filetrs
decouple'''

'''LMS
frontend (react)
backend (django)
virtual env
'''
'''Two terminal one django runserver and another react and same virtual env for both'''


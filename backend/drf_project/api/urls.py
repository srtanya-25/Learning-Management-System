from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include
from accounts.views import RegisterView, DashboardView, LoginView, RefreshView, LogoutView
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, )

router=DefaultRouter()
router.register('students',views.StudentsView) #do not need to put forward slash after students, router does work

#as_view not necessary router knows register url into view
#view set will work always with router(autom url creation)
#router in url and regsiter
router.register('mentors',views.MentorsView)

urlpatterns=[
    path('teachers/',views.teachers_api_view),
    path("teacher/<int:pk>",views.teacher_detail),
    #path('students/',views.StudentsView.as_view()), #class based view
    #path('students',views.StudentsView.as_view()),
    path("",include(router.urls)),
    #path('student/<int:pk>',views.StudentDetail.as_view()) 
    #path('student/<int:student_id>',views.StudentDetail.as_view()) #pk is necessary or else it will not come,if we use some other variable then giive lookup_field=stud_id in views.py
    #path('student/<str:pk>',views.StudentDetail.as_view())  for charfield
    path('mentor/<str:pk>',views.MentorDetail.as_view()),
    path("register/",RegisterView.as_view()),
    # path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/',TokenRefreshView.as_view(), name= 'token_refresh'),
    path("login/", LoginView.as_view()),
    path("refresh/", RefreshView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('dashboard-protected/',DashboardView.as_view())
]


'''ADVANCED CONCEPTS: saves the time,not necessary to create soo many instance methods'''
#MIXINS: alternate way to create class based views, reusable code o create class based views
#GENERICS: 
#127.0.0.1.8000/api/v1/teachers (api endpoint)
#127.0.0.1.8000/teachers/ (web endpoint)
#slug gives limited data
#if char field give string
    #slug: url friendly datatype
    #<int>: datatype integer

'''JWT: Session is not created and sends a token, 
server gives the token to client and is stored via client side. 
and  when request is made the client shares thetoken in the headers to server 
and verifies it and if match then allows.'''

'''access token and refresh token'''
'''access is short lived for 15 mins and referesh is long lived for long duration'''
'''we have to give time duration for specifying'''


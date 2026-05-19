import django_filters  #for case sensitive issue,asCSE but not cse, to get tht, custom filter is made
from .models import Student

class StudentFilter(django_filters.FilterSet):
    branch= django_filters.CharFilter(field_name='branch', lookup_expr='iexact') #IMPORTANT :looku:the method to filter as in xeact is for exact matching but even takes casesensitive, i is for case insensitivity
    student_name= django_filters.CharFilter(field_name='name',lookup_expr='icontains') #icontains 
    id = django_filters.RangeFilter(field_name="student_id", lookup_expr='exact') 
    class Meta:
        model = Student
        fields = ['branch']
    

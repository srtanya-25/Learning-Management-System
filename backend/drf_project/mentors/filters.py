import django_filters  #for case sensitive issue,asCSE but not cse, to get tht, custom filter is made
from .models import Mentor

#this is done as mentor id has text n numbers 
class MentorFilter(django_filters.FilterSet):
    id_min = django_filters.CharFilter(method='filter_by_mentor_id', label="From Mentor ID")
    id_max = django_filters.CharFilter(method='filter_by_mentor_id', label= "To Mentor ID")

    #queryset brings teh data frm db
    def filter_by_mentor_id(self, queryset, name, value):
        if name == "id_min":
            return queryset.filter(mentor_id__gte=value)
        elif name =="id_max":
            return queryset.filter(mentor_id__lte=value)
        return queryset

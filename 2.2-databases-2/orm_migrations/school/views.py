from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    list_student = Student.objects.all().prefetch_related('teachers')
    ordering = 'group'
    context = {
        'object_list': list_student.order_by(ordering)
    }


    return render(request, template, context)

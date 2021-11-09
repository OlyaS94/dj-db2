from django.views.generic import ListView
from django.shortcuts import render

from .models import Student
from .models import Teacher


def students_list(request):
    template = 'school/students_list.html'
    student_list = Student.objects.all().prefetch_related('teacher')
    context = {'object_list': student_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

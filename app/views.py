from django.shortcuts import render

from django.views.generic import ListView
from .models import Group,Students

class GroupView(ListView):
    model = Group
    context_object_name = 'Group'
    template_name = 'index.html'
    
    # def index(request):
    #     group_count = Group.objects.count()
    #     student_count = Students.objects.count()
    #     context = {
    #         'group_count': group_count,
    #         'student_count': student_count
    #     }
    #     return render(request, 'index.html', context)


# def group_student(request,id):
#     group= Group.objects.get(id=id)
#     group = group.group.all()
#     print(group)
#     n = 0 
#     for i in group:
#         print(i)
#         n+= 1
#     return render (request ,"students.html",{"group":group,"n":n})


def themes_quest(request,id):
    theme= Group.objects.get(id=id)
    theme = theme.themes.all()
    print(theme)
    n = 0 
    for i in theme:
        print(i)
        n+= 1
    return render (request ,"students.html",{"theme":theme,"n":n})

def students_in_group(request, group_id):
    group = Group.objects.get(id=group_id)
    students = Students.objects.filter(group=group)
    return render(request, 'students.html', {'group': group, 'students': students})


class StudentView(ListView):
    model = Students
    context_object_name = 'Students'
    template_name = 'students.html'
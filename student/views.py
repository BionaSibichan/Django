from django.shortcuts import render
from student.models import Course
def allStudents(request):
    course="Python Django"
    students=['Biona','Apsa','Sooraj']
    return render(request,'all-students.html',{"my_course":course,"stdlist":students})
    
def home(request):
    course=Course.objects.all()
    print(course)
    return render(request,"index.html",{'all_courses':course})
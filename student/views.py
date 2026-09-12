from django.shortcuts import render

def allStudents(request):
    course="Python Django"
    students=['Biona','Apsa','Sooraj']
    return render(request,'all-students.html',{"my_course":course,"stdlist":students})
    

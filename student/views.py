from django.shortcuts import render,redirect
from student.models import Course,Students

def allStudents(request):
    course="Python Django"
    students=Students.objects.all()
    return render(request,'all-students.html',{"my_course":course,"stdlist":students})
    
def home(request):
    course=Course.objects.all()
    print(course)
    return render(request,"index.html",{'all_courses':course})

def addcourse(request):
    if request.method=="POST":
        course_value=request.POST['course']
        Course(course_name=course_value).save()
        return redirect("/")
    return render(request,"add-course.html")

def addstudent(request):
    courses=Course.objects.all()
    if request.method=="POST":
        student_value=request.POST['student_name']
        phone=request.POST['phone']
        address=request.POST['address']
        dob=request.POST['dob']
        course=request.POST['course']
        course_instance=Course.objects.get(id=course)
        Students(std_name=student_value,phone=phone,address=address,dob=dob,course=course_instance).save()
        return redirect("student:all_stud")
    return render(request,"add-students.html",{"all_courses":courses})

def studentDetails(request,std_id):
    std=Students.objects.get(id=std_id)
    return render(request,"student-details.html",{"student":std})

def editDetails(request, std_id):

    std = Students.objects.get(id=std_id)
    courses = Course.objects.all()

    if request.method == "POST":

        student_value = request.POST['student_name']
        phone = request.POST['phone']
        address = request.POST['address']
        dob = request.POST['dob']
        course = request.POST['course']

        course_instance = Course.objects.get(id=course)

        std.std_name = student_value
        std.phone = phone
        std.address = address
        std.dob = dob
        std.course = course_instance
        std.save()
        return redirect("student:allstud")

    return render(request, "edit-details.html", {
        "student": std,
        "all_courses": courses
    })
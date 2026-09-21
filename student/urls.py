from django.urls import path
from student import views

app_name="student"
urlpatterns=[
    path("",views.home),
    path("all-students",views.allStudents,name="allstud"),
    path("add-course/",views.addcourse,name="add_course"),
    path("add-students/",views.addstudent,name="add_student"),
    path("student-details/<int:std_id>",views.studentDetails,name="student_details"),
    path('edit-details/<int:std_id>', views.editDetails, name='edit_details'),

]
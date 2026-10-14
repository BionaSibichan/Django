from student.models import Course

def listCourses(request):
    courses = Course.objects.all()
    return dict(my_courses=courses)
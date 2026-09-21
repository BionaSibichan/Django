from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=20)

    def __str__(self):
        return self.course_name

class Students(models.Model):
    std_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    dob=models.DateField(max_length=30)
    address=models.CharField(max_length=30)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
            return self.std_name
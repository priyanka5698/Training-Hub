from django.db import models

# Create your models here.
class Regform1(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

Bussiness_Unit = (
    ('eas','EAS'),
    ('analytics', 'Analytics'),
    ('suneralab','Sunera Lab'),
)

class ContactUs(models.Model):
     Name = models.CharField(max_length=100)
     Email = models.CharField(max_length=100)
     Unit = models.CharField(max_length=50, choices=Bussiness_Unit, default='eas')
     Subject = models.CharField(max_length=200)

     def __str__(self):
         return self.Name

class Assignment(models.Model):
    Traineename = models.CharField(max_length=100)
    Totalassignments = models.IntegerField()
    Totalassignmentscompleted = models.IntegerField()
    Totalassignmentspending = models.IntegerField()
    Email = models.EmailField()




    def __str__(self):
        return self.Traineename

CourseName = (
    ('python','Python'),
    ('plsql', 'PlSql'),
    ('Django','Django'),
    ('Node.js','Node.js'),
)

class Assignment1(models.Model):
    TraineeName = models.CharField(max_length=100, verbose_name="Name")
    AssignmentName = models.CharField(max_length=100, verbose_name="Assignment Name")
    CourseName= models.CharField(max_length=50,choices=CourseName, default='Python', verbose_name="Course")

    def __str__(self):
        self.TraineeName

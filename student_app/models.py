from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    personal_email = models.EmailField(blank=True, null= True, unique=True)
    locker_number = models.IntegerField(default=110, unique= True)
    locker_combination = models.CharField(max_length=20, default = "12-12-12", blank=True )
    good_student= models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, new_locker_number):
        self.locker_number = new_locker_number
        self.save()
        return f"Student: {self.student.name}'s locker has been changed to {self.locker_number}"
    def student_status(self, is_good_student):
        self.good_student = is_good_student
        self.save()
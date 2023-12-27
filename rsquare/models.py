from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=10,null=True)
    student_regno=models.IntegerField(primary_key=True,unique=True)
    #student_marks=models.IntegerField()
    
    def __str__(self):
        return f"{self.student_regno}"

class Rank(models.Model):
    #regno,sub1_rank,sub2_rank,sub3_rank
    student_regno=models.ForeignKey(Student,on_delete=models.CASCADE,to_field='student_regno')
    sub1_rank=models.FloatField(max_length=4,null=True)
    sub2_rank=models.FloatField(max_length=4,null=True)
    sub3_rank=models.FloatField(max_length=4,null=True)

    def __str__(self):
        return f"{self.student_regno}"
    
class Grade(models.Model):
    reg_no = models.ForeignKey(Student, on_delete=models.CASCADE,to_field='student_regno')
    sub1_grade = models.CharField(max_length=2)
    sub2_grade = models.CharField(max_length=2)
    sub3_grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.reg_no}"

class Marks(models.Model):
    regno = models.ForeignKey(Student, on_delete=models.CASCADE,to_field='student_regno')
    mark1 = models.IntegerField(default=0)
    mark2 = models.IntegerField(default=0)
    mark3 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.regno}"
    
class EditMarks(models.Model):
    regno = models.ForeignKey(Student, on_delete=models.CASCADE,to_field='student_regno')
    sub = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.regno}"




    


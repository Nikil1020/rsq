
# Create your views here.
import numpy as np
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

class Studentview(APIView):
    def post(self,request):
        serializer = Student_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status = 201)

    def get(self,request,name=None):
        if(name):
            if Student.objects.filter(student_regno=name).exists():
                stu_obj=Student.objects.get(student_regno=name)
                serializer=Student_Serializer(instance=stu_obj)
                return Response(serializer.data,status=201)
            else:
                return Response({"Status_msg":"Doesn't exist"},status = 400)
        else:
            stu_obj=Student.objects.all().order_by('student_regno')
            serializer = Student_Serializer(instance=stu_obj,many=True)
            return Response(serializer.data,status = 201)
        
    def put(self,request,name=None):
        if Student.objects.filter(student_regno=name).exists():
            stu_ob=Student.objects.get(student_regno=name)
            serializer=Student_Serializer(instance=stu_ob,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=201)
            else:
                return Response(serializer.data,status=201)
        else:
            return Response({"Status_msg":"Student doesn't exists"},status=400)
        
    def delete(self,request,name=None):
        if(name):
            if Student.objects.filter(student_regno=name).exists():
                stu_obj=Student.objects.get(student_regno=name)
                stu_obj.delete()
                return Response({"Status_msg":"Delete Successfull"},status=201)
            else:
                return Response({"Status_msg":"Delete unsuccessfull"},status=400)
            

class Rankview(APIView):
    def post(self,request):
        serializer = Rank_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status = 201)
        else:
            return Response({"Status_msg":"post(insertion of stu_reg) failed"},status=400)

    def get(self,request,name=None):
        if(name):
            if Rank.objects.filter(student_regno=name).exists():
                rank_obj=Rank.objects.get(student_regno=name)
                serializer=Rank_Serializer(instance=rank_obj)
                return Response(serializer.data,status=201)
            else:
                return Response({"Status_msg":"Stu_regno Doesn't exist"},status = 400)
        else:
            rank_obj=Rank.objects.all().order_by('student_regno')
            serializer = Rank_Serializer(instance=rank_obj,many=True)
            return Response(serializer.data,status = 201)
        
    def put(self,request,name=None):
        if Rank.objects.filter(student_regno=name).exists():
            rank_obj=Rank.objects.get(student_regno=name)
            serializer=Rank_Serializer(instance=rank_obj,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=201)
            else:
                return Response(serializer.data,status=201)
        else:
            return Response({"Status_msg":"Student_regno doesn't exists"},status=400)
        
    def delete(self,request,name=None):
        if(name):
            if Student.objects.filter(student_regno=name).exists():
                rank_obj=Student.objects.get(student_regno=name)
                rank_obj.delete()
                return Response({"Status_msg":"Deletion of stu_regno Successfull"},status=201)
            else:
                return Response({"Status_msg":"Deletion of stu_regno unsuccessfull"},status=400)
        else:
            rank_obj = Rank.objects.all().order_by('student_regno')
            rank_obj.delete()
            return Response("DELETE SUCCESSFULL", status=201)


class Grade_View(APIView):
    def post(self, request):
        serializer = Grade_Serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"Status_msg":"post(insertion of stu_grade) failed"},status=400)
    
    def get(self, request,name = None):
        if name:
            if Grade.objects.filter(reg_no = name).exists():
                grade_obj = Grade.objects.get(reg_no = name)
                serializer = Grade_Serializer(instance=grade_obj)
                return Response(serializer.data, status=201)
            else:
                return Response({"Status_msg" : "Student does not exist"}, status=400)
        else:
            grade_obj = Grade.objects.all().order_by('reg_no')
            serializer = Grade_Serializer(instance=grade_obj, many = True)
            return Response(serializer.data, status=201)
        
    def put(self,request,name=None):
        if Grade.objects.filter(reg_no=name).exists():
            grade_ob=Grade.objects.get(reg_no=name)
            serializer=Grade_Serializer(instance=grade_ob,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=201)
            else:
                return Response(serializer.data,status=201)
        else:
            return Response({"Status_msg":"Student doesn't exists"},status=400)

    def delete(self,request,name=None):
        if(name):
            if Grade.objects.filter(reg_no=name).exists():
                grade_obj=Grade.objects.get(reg_no=name)
                grade_obj.delete()
                return Response({"Status_msg":"Delete Successfull"},status=201)
            else:
                return Response({"Status_msg":"Delete unsuccessfull"},status=400)
        else:
            grade_obj = Grade.objects.all().order_by('reg_no')
            grade_obj.delete()
            return Response("DELETE SUCCESSFULL", status=201)
    
class Mark_View(APIView):
    def post(self, request):
        serializer = Mark_Serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"Status_msg": "Mark does not exist"}, status = 400)
       
    # def put(self, request, reg = None):
    #     if Marks.objects.filter(regno = reg).exists():
    #         obj = Marks.objects.get(regno = reg)
    #         serializer = Mark_Serializer(instance=obj, data=request.data)
    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save()
    #             return Response(serializer.data, status = 201)
    #     else:
    #         return Response({"Status_msg": "Mark does not exist"}, status = 400)
    # from rest_framework import status


    def put(self, request, reg=None):
        try:
            mark_obj = Marks.objects.get(regno=reg)
        except Marks.DoesNotExist:
            return Response({"Status_msg": "Mark does not exist"}, status=404)
        
        request_data = request.data.copy()  # Make a copy of the request data
        request_data.pop('regno', None)  # Remove 'regno' field from the copy

        serializer = Mark_Serializer(instance=mark_obj, data=request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)




    def get(self, request, reg = None):
        if reg:
            if Marks.objects.filter(regno = reg).exists():
                obj = Marks.objects.get(regno = reg)
                serializer = Mark_Serializer(instance=obj)
                return Response(serializer.data, status=201)
            else:
                return Response({"Status_msg":"Mark does not exist"}, status = 400)
        else:
            obj = Marks.objects.all().order_by('regno')
            serializer = Mark_Serializer(instance=obj, many=True)
            return Response(serializer.data, status=201)
       
    def delete(self, request, reg = None):
        if reg:
            if Marks.objects.filter(regno = reg).exists():
                obj = Marks.objects.get(regno = reg)
                obj.delete()
                return Response({"Status_msg": "Delete Successfull"}, status = 201)
            else:
                return Response({"Status_msg":"Component does not exist"}, status = 400)
        
       
class fetchmark(APIView):
    def post(self,request):
        student_regno_list = list(Student.objects.values_list('student_regno', flat=True))
        mark1_list = []
        mark2_list = []
        mark3_list = []
        for student_regno in student_regno_list:
            student_marks = Marks.objects.filter(regno=student_regno).first()
            if student_marks:
                mark1 = student_marks.mark1
                mark2 = student_marks.mark2
                mark3 = student_marks.mark3
                mark1_list.append(mark1)
                mark2_list.append(mark2)
                mark3_list.append(mark3)
            else:
                print(f"No marks found for student {student_regno}")
        #return Response({"mark1_list": mark1_list})
        minimum = np.min(mark1_list) or np.nan
        maximum = np.max(mark1_list) or np.nan
        percentile_scores = (mark1_list-minimum)/(maximum-minimum)
        minimum2 = np.min(mark2_list) or np.nan
        maximum2 = np.max(mark2_list) or np.nan
        percentile_scores2 = (mark2_list-minimum2)/(maximum2-minimum2)
        minimum3 = np.min(mark3_list) or np.nan
        maximum3 = np.max(mark3_list) or np.nan
        percentile_scores3 = (mark3_list-minimum3)/(maximum3-minimum3)
        percentile_list=[]
        percentile_list2=[]
        percentile_list3=[]
        for l in percentile_scores:
            percentile_list.append('%.2f' % (l))
        for k in percentile_scores2:
            percentile_list2.append('%.2f' % (k))
        for j in percentile_scores3:
            percentile_list3.append('%.2f' % (j))
        for student_regno,p1,p2,p3 in zip(student_regno_list, percentile_list,percentile_list2,percentile_list3):
            data = {
                "student_regno": student_regno,
                "sub1_rank": p1,
                "sub2_rank": p2,
                "sub3_rank": p3
            }
            serializer = Rank_Serializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else:
                print(f"Error saving rank for student {student_regno}: {serializer.errors}")
        serializer = Rank_Serializer(Rank.objects.all(), many=True)  # Serialize all grades
        return Response(serializer.data)
    
        #return Response({"message": "Sub1 ranks posted successfully"})
    def put(self, request):
        student_regno_list = list(Student.objects.values_list('student_regno', flat=True))
        mark1_list = []
        mark2_list = []
        mark3_list = []
        for student_regno in student_regno_list:
            student_marks = Marks.objects.filter(regno=student_regno).first()
            if student_marks:
                mark1 = student_marks.mark1
                mark2 = student_marks.mark2
                mark3 = student_marks.mark3
                mark1_list.append(mark1)
                mark2_list.append(mark2)
                mark3_list.append(mark3)
            else:
                print(f"No marks found for student {student_regno}")

        minimum = np.nanmin(mark1_list)  # Use np.nanmin to handle potential NaN values
        maximum = np.nanmax(mark1_list)
        percentile_scores = (mark1_list - minimum) / (maximum - minimum)

        minimum2 = np.nanmin(mark2_list)
        maximum2 = np.nanmax(mark2_list)
        percentile_scores2 = (mark2_list - minimum2) / (maximum2 - minimum2)

        minimum3 = np.nanmin(mark3_list)
        maximum3 = np.nanmax(mark3_list)
        percentile_scores3 = (mark3_list - minimum3) / (maximum3 - minimum3)

        percentile_list = []
        percentile_list2 = []
        percentile_list3 = []
        for p in percentile_scores:
            percentile_list.append(f"{p:.2f}")
        for p in percentile_scores2:
            percentile_list2.append(f"{p:.2f}")
        for p in percentile_scores3:
            percentile_list3.append(f"{p:.2f}")
        obj=Rank.objects.all()
        for o,student_regno, p1, p2, p3 in zip(obj,student_regno_list, percentile_list, percentile_list2, percentile_list3):
            data = {
                "student_regno": student_regno,
                "sub1_rank": p1,
                "sub2_rank": p2,
                "sub3_rank": p3
            }
            serializer = Rank_Serializer(instance=o,data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else:
                print(f"Error saving rank for student {student_regno}: {serializer.errors}")

        serializer = Rank_Serializer(Rank.objects.all(), many=True)  # Serialize all ranks
        return Response(serializer.data)

class AssignGrades(APIView):
    def post(self, request):
        # Retrieve all student ranks
        ranks = Rank.objects.all()

        # Define desired grade distribution
        grade_distribution = {
            "A": 0.90,  # 90th percentile
            "B": 0.70,  # 70th percentile
            "C": 0.50,  # 50th percentile
            "D": 0.30,  # 30th percentile
            "F": 0.00,  # Below 30th percentile
        }

        # Calculate grade thresholds for each subject
        total_students = ranks.count()
        grade_thresholds = {}
        grade_thresholds = {grade: threshold for grade, threshold in grade_distribution.items()}
        #Assign grades to students based on percentile ranks
        for rank in ranks:
            student_grade = Grade.objects.create(
                reg_no=rank.student_regno,
                sub1_grade=self._assign_grade(rank.student_regno,rank.sub1_rank, grade_thresholds,1),
                sub2_grade=self._assign_grade(rank.student_regno,rank.sub2_rank, grade_thresholds,2),
                sub3_grade=self._assign_grade(rank.student_regno,rank.sub3_rank, grade_thresholds,3),
            )
        serializer = Grade_Serializer(Grade.objects.all(), many=True)  # Serialize all grades
        return Response(serializer.data)

    def _assign_grade(self, reg_no,percentile_rank, grade_thresholds,sub):
        obj = Marks.objects.get(regno=reg_no)
        if sub==1:
            mark=obj.mark1
        elif sub==2:
            mark=obj.mark2
        else:
            mark=obj.mark3
        for grade, threshold in grade_thresholds.items():
            if mark>=50:
                if percentile_rank >= threshold:
                    return grade
                if mark>=50:
                    return "D"
            else:
                return "F"  # Default to "F" if below all thresholds

    def put(self, request, reg=None):
        # 1. Update Marks table
        if Marks.objects.filter(regno=reg).exists():
            obj = Marks.objects.get(regno=reg)
            serializer = Mark_Serializer(instance=obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else:
                return Response({"Status_msg": "Invalid marks data"}, status=400)
        else:
            return Response({"Status_msg": "Mark does not exist"}, status=400)
     # 2. Update Rank table
        fetchmark().put(request)  # Call the PUT method of the fetchmark view
        ranks = Rank.objects.all()
        
        grade_distribution = {
            "A": 0.90,  # 90th percentile
            "B": 0.70,  # 70th percentile
            "C": 0.50,  # 50th percentile
            "D": 0.30,  # 30th percentile
            "F": 0.00,  # Below 30th percentile
        }
        obj=Grade.objects.all()
        obj.delete()
        # Calculate grade thresholds for each subject
        total_students = ranks.count()
        grade_thresholds = {}
        grade_thresholds = {grade: threshold for grade, threshold in grade_distribution.items()}
        #Assign grades to students based on percentile ranks
        for rank in ranks:
            student_grade = Grade.objects.update_or_create(
                reg_no=rank.student_regno,
                sub1_grade=self._assign_grade(rank.student_regno,rank.sub1_rank, grade_thresholds,1),
                sub2_grade=self._assign_grade(rank.student_regno,rank.sub2_rank, grade_thresholds,2),
                sub3_grade=self._assign_grade(rank.student_regno,rank.sub3_rank, grade_thresholds,3),
            )
        serializer = Grade_Serializer(Grade.objects.all(), many=True)  # Serialize all grades
        return Response(serializer.data)
    
class EditMarks_view(APIView):
    def post(self, request):
        serializer = EditMarks_Serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"Status_msg": "editmark doesn't exist"}, status = 400)
        
    def delete(self, request, reg = None):
        if reg:
            if EditMarks.objects.filter(regno = reg).exists():
                obj = EditMarks.objects.get(regno = reg)
                obj.delete()
                return Response({"Status_msg": "Delete Successfull"}, status = 201)
            else:
                return Response({"Status_msg":"Component does not exist"}, status = 400)
            
    def get(self, request, reg = None):
        if reg:
            if EditMarks.objects.filter(regno = reg).exists():
                obj = EditMarks.objects.get(regno = reg)
                serializer = EditMarks_Serializer(instance=obj)
                return Response(serializer.data, status=201)
            else:
                return Response({"Status_msg":"Mark does not exist"}, status = 400)
        else:
            obj = EditMarks.objects.all().order_by('regno')
            serializer = EditMarks_Serializer(instance=obj, many=True)
            return Response(serializer.data, status=201)  
    
class UI_view(APIView):
    def post(self, request):
        serializer = UI_Serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"Status_msg": "editmark doesn't exist"}, status = 400)
        
class Staff_view(APIView):
    def post(self, request):
        serializer = Staff_Serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"Status_msg": "editmark doesn't exist"}, status = 400)
        
class LoginView(APIView):
    def get(self, request, un = None, up=None):
        if un and up:
            if Users.objects.filter(name=un, password=up).exists():
                if Staff.objects.filter(staff_name=un, spassword=up).exists():
                    obj = Staff.objects.get(staff_name=un, spassword=up)
                    serializer = Staff_Serializer(instance=obj)
                    return Response(serializer.data, status=200)    
                else:
                    obj = Users.objects.get(name=un, password=up)
                    serializer = UI_Serializer(instance=obj)
                    return Response(serializer.data, status=201)
            else:
                return Response({"Status_msg":"User does not exist"}, status = 400)
        else:
            return Response({"Status_msg":"User does not exist"}, status = 400)

class RE_view(APIView):
    def post(self, request):
        serializer = RE_Serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"Status_msg": "Mark does not exist"}, status = 400)

    def get(self, request, reg = None):
        if reg:
            if Re_evaluate.objects.filter(regno = reg).exists():
                obj = Re_evaluate.objects.get(regno = reg)
                serializer = RE_Serializer(instance=obj)
                return Response(serializer.data, status=201)
            else:
                return Response({"Status_msg":"Mark does not exist"}, status = 400)
        else:
            obj = Re_evaluate.objects.all().order_by('regno')
            serializer = RE_Serializer(instance=obj, many=True)
            return Response(serializer.data, status=201)
       
    def delete(self, request, reg = None):
        if reg:
            if Re_evaluate.objects.filter(regno = reg).exists():
                obj = Re_evaluate.objects.get(regno = reg)
                obj.delete()
                return Response({"Status_msg": "Delete Successfull"}, status = 201)
            else:
                return Response({"Status_msg":"Component does not exist"}, status = 400)
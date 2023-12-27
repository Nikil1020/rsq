from rest_framework import serializers
from .models import *
class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    #def create(self,validated_data):
     #   return Student.objects.create(**validated_data)

class Rank_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'

class Grade_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class Mark_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'

class EditMarks_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EditMarks
        fields = '__all__'

from django.urls import path
from .views import *

urlpatterns=[
    path('Student/',Studentview.as_view()),
    path('Student/<str:name>',Studentview.as_view()),
    path('Rank/',Rankview.as_view()),
    path('Rank/<int:name>',Rankview.as_view()),
    path('Grade/',Grade_View.as_view()),
    path('Grade/<int:name>',Grade_View.as_view()),
    path('Marks/',Mark_View.as_view()),
    path('Marks/<int:reg>',Mark_View.as_view()),
    path('Fetch/',fetchmark.as_view()),
    path('Grades/',AssignGrades.as_view()),
    path('Grades/<int:reg>',AssignGrades.as_view()),
    path('EditMarks/',EditMarks_view.as_view()),
    path('EditMarks/<int:reg>',EditMarks_view.as_view()),
]
from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Rank)
admin.site.register(Grade)
admin.site.register(Marks)
admin.site.register(EditMarks)
from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
from tinymce import models
# Register your models here.

admin.site.register(Questions)
admin.site.register(StudentsTrial)
admin.site.register(StartExam)
admin.site.register(StudentsProgress)

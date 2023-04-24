from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
from django.utils.html import strip_tags
import uuid

# Create your models here.

class Questions(models.Model):
    # link = "".join(random.choices(string.ascii_letters + string.digits, k  = 7))
    id = models.CharField(max_length = 1000000000000, default =uuid.uuid4, primary_key=True, editable = False)
    question = HTMLField()
    option1 = models.CharField(max_length=1000000)
    option2 = models.CharField(max_length=1000000)
    option3 = models.CharField(max_length=1000000)
    option4 = models.CharField(max_length=1000000)
    answer = models.CharField(max_length=10000000)

    
    def __str__(self):
        return strip_tags(self.question.replace("&nbsp;", " "))
    

class StudentsTrial(models.Model):
    name = models.CharField(max_length=1000000)
    score = models.CharField(max_length=100000)
    date = models.CharField(max_length = 100000, default=datetime.now, blank = False)

    def __str__(self):
        return self.name

class StartExam(models.Model):
    start_exam = models.BooleanField()

class StudentsProgress(models.Model):
    name = models.CharField(max_length = 10000000)
    score = models.CharField(max_length = 100000)
    date = models.CharField(max_length = 100000, default=datetime.now, blank = False)

    def __str__(self):
        return self.name +"; "+ str(self.date)
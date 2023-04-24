from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from datetime import datetime, timedelta

# Create your views here.

# Home Page

def index(request):
    startexam = StartExam.objects.filter(id = 1)[0]
    return render(request, "index.html", {"start": startexam})


# Sign In
def signin(request):
    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]
        user = auth.authenticate(username= username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credential's don't match!")
    return render(request, "signin.html")


# Sign Up
def signup(request):
    if request.method == "POST":
        username = (request.POST['username']).lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username= username).exists():
                messages.info(request, "Username already exists!")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('/signin')
        else:
            messages.info(request, "Passwords don't Match!")
    return render(request, "signup.html")

def exam(request):
    global qsts
    if request.method == "POST":
        if StudentsTrial.objects.filter(name = request.user.username).exists():
            return redirect("/")
        else:
            qsts = Questions.objects.all()

            return render(request, "exam.html", {'questions': qsts})
    else:
        return redirect("/")

def result(request):
    if request.method == "POST":
        if StudentsTrial.objects.filter(name = request.user.username).exists():
            return redirect("/")
        else:
            global qsts
            score = 0
            wrong = 0
            total = 0
            time = datetime.now() + timedelta(hours = 1)

            for abc in qsts:
                total += 1
                if abc.answer == request.POST.get(abc.id):
                    score += 1
                else:
                    wrong+=1

            percentage = round(score/total * 100, 0)

            if percentage <40:
                gp = 0.0
            elif percentage >= 39 and percentage <50:
                gp = 2.0
            elif percentage >= 49 and percentage < 60:
                gp = 3.0
            elif percentage >= 60 and percentage < 70:
                gp = 4.0
            elif percentage > 69:
                gp = 5.0

            percentage = str(percentage)[:-2]

            context = {
                'score':score,
                'wrong': wrong,
                'total': total,
                'percentage':percentage,
                'gp': gp,
                'time':time
            }


            student_score = StudentsTrial.objects.create(name = request.user.username, score = percentage)
            student_score.save()
            students_progress = StudentsProgress.objects.create(name = request.user.username, score=percentage)
            students_progress.save()
            return render(request, 'result.html', context)
    else:
        return redirect("/")
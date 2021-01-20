from django.shortcuts import render
from django.http import HttpResponse
from yaksh.models import AnswerPaper,Course,Question,User
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    ap=AnswerPaper.objects.all()
    user=User.objects.all()
    courseCount=Course.objects.all()
    questionCount=Question.objects.all()
    userCount=User.objects.all()
    contests = [i.name for i in courseCount]
    students = [i.students.all().count() for i in courseCount]
    d=list(tuple(zip(students,contests)))
    d.sort(key=lambda x:x[0])
    studentCount = [i for i,j in d[::-1][:5]]
    contestsName = [j for i,j in d[::-1][:5]]
    moderatorCount=User.objects.filter(groups__name='moderator')
    return render(request,'dashboard.html',{"ap":ap,"user":user,"courseCount":courseCount,\
    "questionCount":questionCount,"userCount":userCount,"moderatorCount":moderatorCount,'contests':contests,'students':students,'studentCount':studentCount,'contestsName':contestsName})

def leaderboard(request):
    courses=Course.objects.all()
    contests=[i for i in courses]
    z = []
    for i in contests:
        answerpapers=AnswerPaper.objects.filter(course = i)
        a=[i.percent for i in answerpapers]
        y = [(i.percent,i.user.username) for i in answerpapers]
        y.sort(key=lambda x:x[0])
        per = [i for i,j in y[::-1][:5]]
        users = [j for i,j in y[::-1][:5]]
        z.append((users,per))
    print(z)    
    return render(request,'leaderboard.html',{"contests":contests,'z':z,'users':users,'per':per})

    

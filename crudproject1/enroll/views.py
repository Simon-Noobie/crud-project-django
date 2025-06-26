from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import StudentRegistration
from .models import User


def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'addNshow.html', {'form': fm,
                                             'stu': stud})

def delete_data(request, id):
    print("-----delete-----")
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/enroll/add_and_show')

def update_data(request, id):
    print("----update--- called")
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance= pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance= pi)
    return render(request, 'updateStudents.html', {'form':fm})
    # Create your views here.

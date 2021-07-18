from django.shortcuts import render, redirect
from app17.models import StudentDetails
import os
from django.contrib import messages

# Create your views here.

def showIndex(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('number')
        photo = request.FILES['photo']
        email = request.POST.get('email')
        StudentDetails(name=name, contact=contact, photo=photo, email=email).save()
        return redirect('home')
    else:
        return render(request, 'home.html')


def showAll(request):
    return render(request, 'admin.html', {"data": StudentDetails.objects.all()})


def showDelete(request, number):
    student_data = StudentDetails.objects.get(number=number)
    if request.method == "POST":
        student_data.delete()
        return render(request, 'admin.html', {"data": StudentDetails.objects.all()})
    else:
        return render(request, 'delete.html', {"data": student_data})


def showUpdatte(request, number):
    student_data = StudentDetails.objects.get(number=number)
    #update = StudentForm(request.POST, instance=student_data)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(student_data.photo) > 0:
                os.remove(student_data.photo.path)
            student_data.photo = request.FILES['photo']
        student_data.name = request.POST.get('name')
        student_data.contact = request.POST.get('contact')
        student_data.email = request.POST.get('email')
        student_data.save()
        messages.success(request, "Profile Update Sucessfully")
        return render(request, 'admin.html', {"data": StudentDetails.objects.all()})
    else:
        return render(request, 'update.html', {"student_data": student_data})

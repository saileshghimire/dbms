from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.http import HttpResponseNotFound
from django.db import connection
# Create your views here.
def base(request):
    data={}
    return render(request,'base/base.html',data)

# def addstudentinformation(request):
#     if request.method == "POST":
#         form = studentinformationsforms()
#         firstname = request.POST.get('firstname')
#         middlename = request.POST.get('middlename')
#         lastname = request.POST.get('lastname')
#         Gender = request.POST.get('Gender')
#         rollnumber = request.POST.get('rollnumber')
#         phonenumber = request.POST.get('phonenumber')
#         DateofBirth = request.POST.get('DateofBirth')
#         email = request.POST.get('email')
#         fathername = request.POST.get('fathername')
#         mothername = request.POST.get('mothername')
#         DateofAdmission = request.POST.get('DateofAdmission')
#         Fees = request.POST.get('Fees')
#         cursor = connection.cursor()
#         cursor.execute("INSERT INTO base_studentdetail(firstname,middlename,lastname,Gender,rollnumber,phonenumber,DateofBirth,email,fathername,mothername,DateofAdmission,Fees) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",['%{}%'.format(firstname),'%{}%'.format(middlename),'%{}%'.format(lastname),'%{}%'.format(Gender),'%{}%'.format(rollnumber),'%{}%'.format(phonenumber),'%{}%'.format(DateofBirth),'%{}%'.format(email),'%{}%'.format(fathername),'%{}%'.format(mothername),'%{}%'.format(DateofAdmission),'%{}%'.format(Fees)])
       
#     else:
#         form = studentinformationsforms()
#     return render(request,'base/addstudent.html',{'form':form})

def addstudentinformation(request):
    if request.method == "POST":
        form = studentinformationsforms(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            middlename = form.cleaned_data['middlename']
            lastname = form.cleaned_data['lastname']
            Gender = form.cleaned_data['Gender']
            rollnumber = form.cleaned_data['rollnumber']
            phonenumber = form.cleaned_data['phonenumber']
            DateofBirth = form.cleaned_data['DateofBirth']
            email = form.cleaned_data['email']
            fathername = form.cleaned_data['fathername']
            mothername = form.cleaned_data['mothername']
            DateofAdmission = form.cleaned_data['DateofAdmission']
            Fees = form.cleaned_data['Fees']
            cursor = connection.cursor()
            cursor.execute("INSERT INTO base_studentdetail(firstname,middlename,lastname,Gender,rollnumber,phonenumber,DateofBirth,email,fathername,mothername,DateofAdmission,Fees) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (firstname, middlename, lastname, Gender, rollnumber, phonenumber, DateofBirth, email, fathername, mothername, DateofAdmission, Fees))
            return redirect('view')
    else:
        form = studentinformationsforms()
    return render(request,'base/addstudent.html',{'form':form})



def searchstudent(request):
    keyword = request.GET.get('keyword')
    rows = []
    if keyword is not None:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM base_studentdetail WHERE firstname LIKE %s",['%{}%'.format(keyword)])
        rows = cursor.fetchall()
    else:
        cursor = connection.cursor()
        cursor.execute("SELECT* FROM base_studentdetail")
        rows = cursor.fetchall()
    return render(request,'base/search.html',{'rows':rows})



def updatestudent(request, id):
    student = StudentDetail.objects.get(id=id)
    if request.method == "POST":
        form = studentinformationsforms(request.POST, instance=student)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            middlename = form.cleaned_data['middlename']
            lastname = form.cleaned_data['lastname']
            Gender = form.cleaned_data['Gender']
            rollnumber = form.cleaned_data['rollnumber']
            phonenumber = form.cleaned_data['phonenumber']
            DateofBirth = form.cleaned_data['DateofBirth']
            email = form.cleaned_data['email']
            fathername = form.cleaned_data['fathername']
            mothername = form.cleaned_data['mothername']
            DateofAdmission = form.cleaned_data['DateofAdmission']
            Fees = form.cleaned_data['Fees']
            cursor = connection.cursor()           
            cursor.execute("""
                           UPDATE base_studentdetail 
                SET 
                    firstname = %s, 
                    middlename = %s, 
                    lastname = %s, 
                    Gender = %s, 
                    rollnumber = %s, 
                    phonenumber = %s, 
                    DateofBirth = %s, 
                    email = %s, 
                    fathername = %s, 
                    mothername = %s, 
                    DateofAdmission = %s, 
                    Fees = %s
                WHERE id = %s""",(
                firstname, 
                middlename, 
                lastname, 
                Gender, 
                rollnumber, 
                phonenumber, 
                DateofBirth, 
                email, 
                fathername, 
                mothername, 
                DateofAdmission, 
                Fees, 
                id
            ))
            return redirect('view')
    else:
        form = studentinformationsforms(instance=student)
    return render(request, 'base/update.html', {'form': form, 'student': student})



def deletestudent(request):
    keyword = request.GET.get('keyword')
    try:
        student = StudentDetail.objects.get(firstname=keyword)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM base_studentdetail WHERE id=%s", [student.id])
        connection.commit()
        return render(request, 'base/delete.html')
    except StudentDetail.DoesNotExist:
        return render(request, 'base/delete.html')


def viewdata(request):
    cursor = connection.cursor()
    cursor.execute("SELECT* FROM base_studentdetail")
    rows = cursor.fetchall()
    return render(request,'base/views.html',{'rows':rows})
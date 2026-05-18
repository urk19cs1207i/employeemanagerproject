from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app1.models import AddEmployee
from app1.forms import AddEmployeeForm, SignupForm
from app1.models import CalenderEvent
from app1.forms import CalenderEventForm
from app1.models import AddLatestNews
from app1.forms import AddLastestNewsForm
from app1.models import AddJobOpening 
from app1.forms import AddJobOpeningForm
from django.http import HttpResponse, HttpResponseRedirect 
import csv


# Create your views here.

def homeview(request):
    response = render(request,"app1/home.html")
    return response

@login_required
def hrmanagerview(request):
    response=render(request, "app1/hr_manager.html")
    return response

def employeeview(request):
    response=render(request, "app1/employee.html")
    return response 

def addempview(request):
    form=AddEmployeeForm()
    if request.method=='POST':
        form=AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/hrmanager/")
    response=render(request,'app1/addemp.html', {'form': form})
    return response 

def addnewcalview(request):
    form=CalenderEventForm()
    if request.method=='POST':
        form=CalenderEventForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/calenderholiday/")
    response=render(request,'app1/addnewcal.html', {'form':form})
    return response 

def addnewsview(request):
    form=AddLastestNewsForm()
    if request.method == "POST":
        form=AddLastestNewsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/latestnews/')
    response=render(request,'app1/addnews.html', {'form':form})
    return response 

def empdataview(request):
    data=AddEmployee.objects.all()
    response=render(request, 'app1/empdata.html', {'d':data})
    return response

def jobopeningview(request):
    form=AddJobOpeningForm()
    if request.method == "POST":
        form=AddJobOpeningForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/jobdetails/")
    response=render(request,'app1/jobopening.html',{'form':form})
    return response 

def deleteview(request,id):
    data=AddEmployee.objects.get(id=id)
    data.delete()
    return redirect("/empdata/")
    
def updateview(request,id):
    emp=AddEmployee.objects.get(id=id)
    form = AddEmployeeForm(instance=emp) 
    if request.method=="POST":
        form=AddEmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect("/empdata/")
    return render(request, "app1/update.html", {'form':form})

def calenderholidayview(request):
    data=CalenderEvent.objects.all()
    response=render(request,'app1/calenderholiday.html',{'d':data})
    return response

def latestnewsview(request):
    data=AddLatestNews.objects.all()
    response=render(request,'app1/latestnews.html', {'d':data})
    return response

def latestnewsdeleteview(request,id):
    data=AddLatestNews.objects.get(id=id)
    data.delete()
    return redirect("/latestnews/")

def latestnewsupdateview(request,id):
    news=AddLatestNews.objects.get(id=id)
    form=AddLastestNewsForm(instance=news)
    if request.method=='POST':
        form=AddLastestNewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect("/latestnews/")
    return render(request, "app1/latestnewsupdate.html", {'form':form})


def jobdetailsview(request):
    data = AddJobOpening.objects.all()
    response=render(request,'app1/jobdetails.html',{'d':data})
    return response

def getdataview(request):
    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition']='attachment; filename="employeelist.csv"'
    emp=AddEmployee.objects.all()

    writer=csv.writer(response)
    writer.writerow(['ID','Name','Designation','Date of Joining','Department','Annual CTC', 'Experience'])

    for employee in emp:
        writer.writerow([employee.empid,employee.fullname,employee.designation, " " + str(employee.date) if employee.date else '',employee.department,employee.annualctc,employee.experience])

    return response

def thanksview(request):
    response=render(request,'app1/logout.html')
    return response

def logoutview(request):
    logout(request)
    return redirect("/thanks/")

def userview(request): 
    if request.method == 'POST': 
        form = SignupForm(request.POST) 
        if form.is_valid(): 
            user=form.save(commit=False) 
            user.set_password(form.cleaned_data['password'])
            user.save() 
            return HttpResponseRedirect("/accounts/login/") 
        else:
            print(form.errors)   
        
    else:
        form = SignupForm()
    return render(request, 'app1/register.html', {'form': form})
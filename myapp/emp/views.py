from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp,Attendance,Emp_Attendances
from .models import Customer
from .forms import CustomerRegistractionForms,CustomerProfileForm,Employee_Attendance,Emp_Attendance
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime
#from .models import Attendance


def emp_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})


def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    print("Yes Bhai")
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
    return redirect("/emp/home/")




#adding new fetures




class CustomerRegistrationView(View):
 def get(self,request):
  form=CustomerRegistractionForms()
  return render(request,'emp/customerregistration.html',{'form':form})
 def post(self,request):
  form=CustomerRegistractionForms(request.POST)
  if  form.is_valid():
   messages.success(request,'Congulation you have register succesfully')
   form.save()
  return render(request,'emp/customerregistration.html',{'form':form})
 


@method_decorator(login_required,name='dispatch')
class ProfileView(View):
	def get(self, request):
		form = CustomerProfileForm()
		return render(request, 'emp/profile.html', {'form':form, 'active':'btn-primary'})
		
	def post(self,request):
		form = CustomerProfileForm(request.POST)
		if form.is_valid():
			usr = request.user
			name  = form.cleaned_data['name']
			locality = form.cleaned_data['locality']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zipcode = form.cleaned_data['zipcode']
			reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
			reg.save()
			messages.success(request, 'Congratulations!! Profile Updated Successfully.')
		return render(request, 'emp/profile.html', {'form':form, 'active':'btn-primary'})





@method_decorator(login_required,name='dispatch')
class Employees_Attendence(View):
    def get(self,request):
        form=Employee_Attendance()
        return render (request,'emp/Attendance.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form=Employee_Attendance(request.POST)
        if form.is_valid():
            usr=request.user
            print(form.cleaned_data)
            attendence=form.cleaned_data['attendance']
            #checkin=form.cleaned_data['check_in']
            #checkout=form.cleaned_data['checkout']
            date_time=form.cleaned_data['date_time']
            reg = Attendance(user=usr,attendance=attendence,date_time=date_time)
            reg.save()
            res= datetime.now()
            messages.success(request, f'Attendence Updated Successfully at {res}.')
        return render(request, 'emp/Attendance.html', {'form':form, 'active':'btn-primary'})





@method_decorator(login_required,name='dispatch')
class Emp_Attendence(View):
    def get(self,request):
        form=Emp_Attendance()
        return render (request,'emp/Attendance.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form=Emp_Attendance(request.POST)
        if form.is_valid():
            usr=request.user
            print(form.cleaned_data)
            attendence=form.cleaned_data['attendance']
            checkin=form.cleaned_data['check_in']
            checkout=form.cleaned_data['checkout']
            #date_time=form.cleaned_data['date_time']
            reg = Emp_Attendances(user=usr,attendance=attendence,check_in=checkin,checkout=checkout)
            reg.save()
            res= datetime.now()
            messages.success(request, f'Attendence Updated Successfully at {res}.')
        return render(request, 'emp/Attendance.html', {'form':form, 'active':'btn-primary'})



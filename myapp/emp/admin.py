from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Emp)
class EmpModelAdmin(admin.ModelAdmin):
    list_display=['id','name','emp_id','phone','address','working','department']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']




@admin.register(Attendance)
class AttendanceModelAdmin(admin.ModelAdmin):
    list_display=['id','user','attendance','date_time']



@admin.register(Emp_Attendances)
class EmpAttendanceModelAdmin(admin.ModelAdmin):
    list_display=['id','user','attendance','check_in']

from django.contrib import admin
from app1.models import AddEmployee
from app1.models import CalenderEvent
from app1.models import AddLatestNews
from app1.models import AddJobOpening

# Register your models here.
class AddEmployeeAdmin(admin.ModelAdmin):
    list_display=['fullname', 'empid', 'designation', 'date', 'department', 'annualctc', 'experience']
admin.site.register(AddEmployee, AddEmployeeAdmin)

class AddLatestNewsAdmin(admin.ModelAdmin):
    list_display=['details']
admin.site.register(AddLatestNews, AddLatestNewsAdmin)

class CalenderEventAdmin(admin.ModelAdmin):
    list_display=['date','occasion']
admin.site.register(CalenderEvent, CalenderEventAdmin)


class AddJobOpeningAdmin(admin.ModelAdmin):
    list_display=['job','experience','skill','currentctc','noticeperiod']
admin.site.register(AddJobOpening, AddJobOpeningAdmin)
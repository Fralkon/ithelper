from django.contrib import admin
from monitoring.models import User, Info, Equipment, Equipment_type,Branch,Printer,ServiceOrganization,Task,PrinterModel

# Register your models here.
@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Info)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(Equipment)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(Equipment_type)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(Branch)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(ServiceOrganization)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(PrinterModel)
class GradeAdmin(admin.ModelAdmin):

    pass
@admin.register(Printer)
class GradeAdmin(admin.ModelAdmin):
    pass
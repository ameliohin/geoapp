from django.contrib import admin
from .models import Branch, Employee

class EmployeeInLine(admin.TabularInline):
    model = Employee

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    inlines = [EmployeeInLine,]

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name',)
    list_display = ('first_name', 'last_name', 'position_title')


admin.site.register(Branch, BranchAdmin)
admin.site.register(Employee, EmployeeAdmin)
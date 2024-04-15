from django.contrib import admin
from .models import ParentModel, ChildModel, ClassModel, EnrollModel


# Register your models here.

@admin.register(ParentModel)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


@admin.register(ChildModel)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'parent')
    search_fields = ('name',)
    list_filter = ('parent',)


@admin.register(ClassModel)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'seats')
    search_fields = ('name',)
    list_filter = ('seats',)


@admin.register(EnrollModel)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('id','child', 'class_enrolled', 'enrollment_date')
    search_fields = ('child__name', 'class_enrolled__name')
    list_filter = ('enrollment_date',)

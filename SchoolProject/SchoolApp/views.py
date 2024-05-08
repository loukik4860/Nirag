from django.shortcuts import render, redirect
from .forms import ParentForm, ChildForm, EnrollForm, ClassForm, SubjectForm
from .models import *
from django.db.models import Q
from django.contrib import messages
import time
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import logging

logger = logging.getLogger("SchoolApp.views")


def homeView(request):
    template_name = "SchoolApp/Home.html"
    parents = None
    try:
        search_post = request.GET.get('search')
        print(search_post)
        if search_post:
            parents = ParentModel.objects.filter(Q(name__icontains=search_post) | Q(email__icontains=search_post))
        else:
            raise ValidationError("Search parameter is missing.")
    except ValidationError as e:
        # Handle the validation error here
        print("Validation Error:", e)
    return render(request, template_name, {'parents': parents})


@login_required(login_url='account/login')
def add_parents(request):
    form = ParentForm()
    template_name = "SchoolApp/parentForm.html"
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            time.sleep(3)
            messages.success(request, "Parents Data has been saved")
            return redirect('addStudent')
        else:
            messages.error(request, "Some error has occured try again")
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='account/login')
def updateParents(request, pk=None):
    logger.info('Processing request in my_view')

    parent = ParentModel.objects.get(id=pk)
    form = ParentForm(instance=parent)
    template_name = 'SchoolApp/parentForm.html'
    context = {'form': form, 'parent': parent}
    if request.method == "POST":
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            time.sleep(3)
            messages.success(request, 'data has been updated')
            logger.info("parents data has beeen saved")
        else:
            messages.error(request, 'error has occured')
            logger.error("error occured at saving parent model")
    return render(request, template_name, context)


@login_required(login_url='account/login')
def parentsList(request):
    parents = ParentModel.objects.all()
    template_name = 'SchoolApp/parentsList.html'
    context = {'parents': parents}
    return render(request, template_name, context)


@login_required(login_url='account/login')
def deleteParent(request, pk=None):
    parents = ParentModel.objects.get(id=pk)
    parents.delete()
    return redirect('parentsList')


@login_required(login_url='account/login')
def add_student(request):
    form = ChildForm()
    template_name = "SchoolApp/studentForm.html"
    if request.method == "POST":
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Parents Data has been saved")
            time.sleep(3)
            return redirect('enrollStudent')
        else:
            messages.error(request, "Some error has occurred try again")
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='account/login')
def studentList(request):
    student = ChildModel.objects.all()
    paginator = Paginator(student, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'SchoolApp/studentList.html'
    context = {'page_obj': page_obj}
    return render(request, template_name, context)


@login_required(login_url='account/login')
def updateStudent(request, pk=None):
    student = ChildModel.objects.get(id=pk)
    form = ChildForm(instance=student)
    template_name = 'SchoolApp/studentForm.html'
    context = {'form': form, 'student': student}
    if request.method == "POST":
        form = ParentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            time.sleep(3)
            messages.success(request, 'data has been updated')
        else:
            messages.error(request, 'error has occured')
    return render(request, template_name, context)


@login_required(login_url='account/login')
def deleteStudent(request, pk=None):
    student = ChildModel.objects.get(id=pk)
    student.delete()
    return redirect('studentList')


@login_required(login_url='account/login')
def add_Class(request):
    form = ClassForm()
    template_name = "SchoolApp/addClass.html"
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            time.sleep(3)
            messages.success(request, "Class Data has been saved")
            return redirect('addparents')
        else:
            messages.error(request, "Some error has occurred try again")
    context = {'form': form}
    print("added")
    return render(request, template_name, context)


@login_required(login_url='account/login')
def classList(request):
    Class = ClassModel.objects.all()
    template_name = 'SchoolApp/ClassList.html'
    context = {'Class': Class}
    return render(request, template_name, context)


@login_required(login_url='account/login')
def updateClass(request, pk=None):
    Class = ClassModel.objects.get(id=pk)
    form = ClassForm(instance=Class)
    template_name = 'SchoolApp/addClass.html'
    context = {'form': form, 'Class': Class}
    if request.method == "POST":
        form = ParentForm(request.POST, instance=Class)
        if form.is_valid():
            form.save()
            time.sleep(3)
            messages.success(request, 'data has been updated')
        else:
            messages.error(request, 'error has occurred')
    return render(request, template_name, context)


@login_required(login_url='account/login')
def deleteClass(request, pk=None):
    Class = ClassModel.objects.get(id=pk)
    Class.delete()
    return redirect('classList')


@login_required(login_url='account/login')
def ClassEnrolledView(request):
    form = EnrollForm()
    template_name = "SchoolApp/ClassEnroll.html"
    if request.method == "POST":
        form = EnrollForm(request.POST)
        if form.is_valid():
            form.save()
            time.sleep(3)
            messages.success(request, "Parents Data has been saved")
            return redirect('classList')
        else:
            messages.error(request, "Some error has occurred try again")
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='account/login')
def ClassStudent(request, pk=None):
    student = EnrollModel.objects.filter(class_enrolled__id=pk)
    template_name = 'SchoolApp/classStudent.html'
    context = {'student': student}
    return render(request, template_name, context)


@login_required(login_url='account/login')
def unenrolledClass(request, pk=None):
    student = EnrollModel.objects.filter(class_enrolled__id=pk)
    student.delete()
    return redirect('enrollStudent')


def subjectEnrolledView(request):
    form = SubjectForm()
    template_name = "SchoolApp/SubjectEnroll.html"
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            time.sleep(3)
            messages.success(request, "Subject Data has been saved")
            return redirect('studentList')
        else:
            messages.error(request, "Some error has occurred try again")
    context = {'form': form}
    print("added")
    return render(request, template_name, context)


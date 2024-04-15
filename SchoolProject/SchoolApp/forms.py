from django import forms
from django.forms import ModelForm
from .models import EnrollModel, ParentModel, ChildModel, ClassModel


class ParentForm(forms.ModelForm):
    class Meta:
        model = ParentModel
        fields = ['name', 'email']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


class ChildForm(ModelForm):
    class Meta:
        model = ChildModel
        fields = ['name', 'age', 'parent']
        labels = {
            'name': 'NAME',
            'age': 'Age',
            'parent': 'Parents'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-select'})
        }


class ClassForm(ModelForm):
    class Meta:
        model = ClassModel
        fields = ['name', 'description', 'seats']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'seats': 'Seats'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2', 'rows': 5}),
            'seats': forms.TextInput(attrs={'class': 'form-select my-2', 'readonly': True})
        }


class EnrollForm(ModelForm):
    class Meta:
        model = EnrollModel
        fields = ['child', 'class_enrolled']

        labels = {
            'child': 'Student',
            'class_enrolled': 'Class'
        }
        widgets = {
            'child': forms.Select(attrs={'class': 'form-select my-2'}),
            'class_enrolled': forms.Select(attrs={'class': 'form-select my-2'})
        }

        def clean(self):
            cleaned_data = super().clean()
            class_enrolled = cleaned_data.get('class_enrolled')
            if class_enrolled:
                enrolled_count = EnrollModel.objects.filter(class_enrolled=class_enrolled).count()
                total_seats = class_enrolled.seats
                if enrolled_count >= total_seats:
                    raise forms.ValidationError("The class has reached its maximum capacity.")

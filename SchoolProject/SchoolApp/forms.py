from django import forms
from django.forms import ModelForm
from .models import EnrollModel, ParentModel, ChildModel, ClassModel, SubjectModel, historicalData
from django.core import validators


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


class SubjectForm(forms.ModelForm):
    class Meta:
        model = SubjectModel
        fields = "__all__"
        labels = {
            'child': 'Child',
            'english': 'English',
            'mathematics': 'Mathematics',
            'chemistry': 'Chemistry',
            'biology': 'Biology',
            'history': 'History',
            'geography': 'Geography',
            'politics': 'Politics'
        }
        widgets = {
            'child': forms.Select(attrs={'class': 'form-select my-2'}),
            'english': forms.NumberInput(attrs={'class': 'form-control'}),
            'mathematics': forms.NumberInput(attrs={'class': 'form-control'}),
            'chemistry': forms.NumberInput(attrs={'class': 'form-control'}),
            'biology': forms.NumberInput(attrs={'class': 'form-control'}),
            'history': forms.NumberInput(attrs={'class': 'form-control'}),
            'geography': forms.NumberInput(attrs={'class': 'form-control'}),
            'politics': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_english(self):
        english = self.cleaned_data['english']
        if english > 100 or english < 0:
            print("clean_english")
            raise validators.ValidationError("Marks should not be more than 100 and less than zero ('0')")
        return english

    def clean_mathematics(self):
        mathematics = self.cleaned_data['mathematics']
        if mathematics > 100 or mathematics < 0:
            print("clean_mathematics")
            raise validators.ValidationError("Marks should not be more than 100 and less than zero ('0')")
        return mathematics

from django.db import models
from django.core.exceptions import ValidationError


class ParentModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    def clean(self):
        if ParentModel.objects.filter(name=self.name, email=self.email).exists():
            raise ValidationError("This Parents already enrolled in.")


class ChildModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ClassModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    seats = models.IntegerField(default=40)

    def __str__(self):
        return self.name

    def clean(self):
        if self.seats > 40:
            raise ValidationError("Number of seats cannot exceed 4")


class EnrollModel(models.Model):
    child = models.ForeignKey(ChildModel, on_delete=models.CASCADE, related_name="child")
    class_enrolled = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='classEnrolled')
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.child.name} enrolled in {self.class_enrolled.name}"

    def clean(self):
        if EnrollModel.objects.filter(child=self.child).exists():
            raise ValidationError("This student is already enrolled in another class.")

        if EnrollModel.objects.filter(child=self.child, class_enrolled=self.class_enrolled).exists():
            raise ValidationError("This student is already enrolled in this class.")

        enrolled_count = EnrollModel.objects.filter(class_enrolled=self.class_enrolled).count()
        if enrolled_count >= 40:
            raise ValidationError(
                "The class has reached its maximum capacity of 40 students You cannot Enroll Any more student.")


class SubjectModel(models.Model):
    child = models.ForeignKey(ChildModel, on_delete=models.CASCADE, related_name='subject')
    english = models.FloatField()
    mathematics = models.FloatField()
    chemistry = models.FloatField()
    biology = models.FloatField()
    history = models.FloatField()
    geography = models.FloatField()
    politics = models.FloatField()


class historicalData(models.Model):
    child = models.ForeignKey(ChildModel, on_delete=models.CASCADE, related_name='historicalData')
    year = models.DateField()
    percentage = models.FloatField(null=True,blank=True)

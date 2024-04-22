from django.urls import path
from .views import add_parents, updateParents, parentsList, deleteParent, homeView, \
    add_student, studentList, updateStudent, deleteStudent, add_Class, classList, updateClass, \
    deleteClass, ClassEnrolledView, ClassStudent,unenrolledClass

urlpatterns = [
    path('home/', homeView, name="home"),
    path('parentslist/', parentsList, name="parentsList"),
    path('addparents/', add_parents, name="addparents"),
    path('updateparents/<int:pk>/', updateParents, name="updateparents"),
    path('deleteparent/<int:pk>/', deleteParent, name="deleteparent"),
    path('addstudent/', add_student, name="addStudent"),
    path('studentList/', studentList, name="studentList"),
    path('updateStudent/<int:pk>/', updateStudent, name="updateStudent"),
    path('deleteStudent/<int:pk>/', deleteStudent, name="deleteStudent"),
    path('classList/', classList, name="classList"),
    path('addClass/', add_Class, name="addClass"),
    path('updateClass/<int:pk>/', updateClass, name="updateClass"),
    path('classDelete/<int:pk>/', deleteClass, name="classDelete"),
    path('enrollStudent/', ClassEnrolledView, name="enrollStudent"),
    path('classEnrolledStudent/<int:pk>/', ClassStudent, name="classStudent"),
    path('unenrolledStudent/<int:pk>/',unenrolledClass,name="unEnrolledClass")
]

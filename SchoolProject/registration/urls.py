from django.urls import path
from .views import registerVeiw,registration_success,loginView,logoutView

urlpatterns = [
    path('register/', registerVeiw, name='register'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('registration-success/', registration_success, name='registration_success'),
]

from django.urls import path
from .views import registerVeiw,registration_success,loginView

urlpatterns = [
    path('register/', registerVeiw, name='register'),
    path('login/', loginView, name='login'),
    path('registration-success/', registration_success, name='registration_success'),
]

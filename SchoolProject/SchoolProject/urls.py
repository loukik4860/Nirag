from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('school/', include("SchoolApp.urls")),
    path('account/', include("registration.urls")),
    # path('accounts/',include("django.contrib.auth.urls"))
] + static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)

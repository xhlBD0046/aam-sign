# mysite/urls.py
from django.contrib import admin
from django.urls import path
from .views import under_construction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', under_construction, name='home'),
]

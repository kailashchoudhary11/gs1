from django.urls import path
from .views import student_detail
app_name = "api"

urlpatterns = [
    path("", student_detail, name="student_detail"),
]

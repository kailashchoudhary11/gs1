from django.urls import path
from .views import student_detail, student_list
app_name = "api"

urlpatterns = [
    path("<int:pk>/", student_detail, name="student_detail"),
    path("all/", student_list, name="student_list"),
]

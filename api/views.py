from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
# Create your views here.


# Single Model Object 

def student_detail(request):
    student = Student.objects.get(id=3)
    serializer = StudentSerializer(student)
    print(serializer.data)
    # print(type(serializer.data))
    # print(dict(student)) # This is not possible
    print(dict(serializer.data)) # This is possible
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    # return JsonResponse(serializer.data)
    return HttpResponse(json_data, content_type="application/json")

def student_list(request):
    students = Student.objects.all()
    serializers = StudentSerializer(students, many=True)
    for serializer in serializers:
        print(serializer.data)
    return HttpResponse("Hello, World")
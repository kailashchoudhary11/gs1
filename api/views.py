from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
# Create your views here.


# Single Model Object 

def student_detail(request, pk):
    student = Student.objects.get(id=pk)
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
    json_data = JSONRenderer().render(serializers.data)
    print(json_data)
    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serializers.data, safe=False)
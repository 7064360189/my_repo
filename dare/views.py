from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse






# Create your views here.
def student(request,s):
    stu= Student.objects.get(id=s)
    # print(stu)

    serializer= StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)

    json_data=JSONRenderer().render(serializer.data)
    # print(json_data)

    return HttpResponse(json_data,content_type='application/json')

# queryset

def student_details(request,):
    stu= Student.objects.all()
    # print(stu)

    serializer= StudentSerializer(stu,many=True)
    # print(serializer)
    # print(serializer.data)

    # json_data=JSONRenderer().render(serializer.data)
    # print(json_data)

    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)



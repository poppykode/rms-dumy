from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)
from rest_framework.response import Response
from .serializers import StudentSerializer,StudentResultSerializer
from students.models import Student,StudentResult
from rms.utils import generate_achieve_id
############################################################################################
# Student Related APIs

@csrf_exempt
@api_view(['POST'])
def create_student(request):
    if request.method =='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(archieve_id=generate_achieve_id())
            return Response(serializer.data, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_student(request,id):
    try:
        qs = Student.objects.get(student_id=id)
    except Student.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = StudentSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_student_result(request):
    if request.method =='POST':
        serializer = StudentResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(archieve_id=generate_achieve_id())
            return Response(serializer.data, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_student_result(request,id):
    try:
        qs = StudentResult.objects.get(student_result_id=id)
    except Student.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = StudentResultSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_400_BAD_REQUEST)
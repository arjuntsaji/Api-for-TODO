from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializers
from .models import Todo


# Create your views here.
@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-details/<str:pk>/',
        'Create': '/task-create',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Todo.objects.all()
    serializer = TodoSerializers(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Todo.objects.get(id=pk)
    serializer = TodoSerializers(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
    task=Todo.objects.get(id=pk)
    serializer=TodoSerializers(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer=TodoSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['Delete'])
def taskDelete(request,pk):
    task=Todo.objects.get(id=pk)
    task.delete()
    return Response("task delete successfully")


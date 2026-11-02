from django.shortcuts import render, redirect
from .models import Task
from todo.serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def home(request):
    all_tasks = Task.objects.all()
    return render(request, 'home.html', {'task': all_tasks})


def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')

        Task.objects.create(
            task_name=task_name
        )

        return redirect('todo:home')

    return render(request, 'add_task.html')


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task_name = request.POST.get('task_name','').strip()
        if task_name:
            task.task_name = task_name
            task.save(update_fields=['task_name'])
        if request.POST.get('completed'):
            task.completed = True
        else:
            task.completed = False

        task.save()

        return redirect('todo:home')

    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todo:home')

@api_view(['GET', 'POST'])
def ListCreateTask(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def task_detail(request, pk):
    try:
        snippet = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TaskSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
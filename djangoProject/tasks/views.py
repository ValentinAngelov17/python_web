from django.shortcuts import render
from django.http import HttpResponse
from djangoProject.tasks.models import Task

# Create your views here.


def index(request):
    return HttpResponse("It works!")


def list_task(request):
    tasks_list = Task.objects.all()
    output = '; '.join(f"{t.title}: {t.description} {t.priority}" for t in tasks_list)

    if not output:
        output = "There are no created tasks!"

    return HttpResponse(output)


def list_task_templete(request):
    context = {
        'text': 'My tasks for today!',
        'tasks': Task.objects.order_by('id').all()

    }
    return render(request, 'tasks.html', context=context)

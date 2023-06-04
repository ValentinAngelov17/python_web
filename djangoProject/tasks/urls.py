#urls for tasks app
from django.urls import path
from djangoProject.tasks.views import index, list_task, list_task_templete

urlpatterns = [
    path('', index),
    path('lists/', list_task),
    path('with-templete', list_task_templete)
]

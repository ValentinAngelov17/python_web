from django.contrib import admin
from djangoProject.tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'priority')


admin.site.register(Task, TaskAdmin)


from django.contrib import admin

# Register your models here.
from tasks.models import Task
admin.site.register(Task)
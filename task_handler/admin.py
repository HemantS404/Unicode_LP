from typing import List
from django.contrib import admin
from .models import task

class Ts(admin.ModelAdmin):
    list_display = ('user','title','description','complete','create')
    search_fields = ('title',)

admin.site.register(task, Ts)

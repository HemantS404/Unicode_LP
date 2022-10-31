from django.contrib import admin
from .models import User

class Us(admin.ModelAdmin):
    list_display = ('username','email','is_staff')
    search_fields = ('username','email')

admin.site.register(User, Us)

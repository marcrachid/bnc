from django.contrib import admin
from .models import Circuit


class CircuitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title']
# Register your models here.

admin.site.register(Circuit, CircuitAdmin)

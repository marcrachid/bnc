from django.shortcuts import render
from django.http import HttpResponse
from .models import Circuit

# Create your views here.


def index(request):
    """circuits = Circuit.objects.all()
    circuit_titles = [circuit.title for circuit in circuits]
    circuit_titles_str = ", ".join(circuit_titles)
    return HttpResponse("Les circuits : " + circuit_titles_str)"""
    circuits = Circuit.objects.all()
    return render(request, 'ecotourism/index.html', {'circuits': circuits})

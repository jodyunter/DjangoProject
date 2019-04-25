import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def teams(request):
    return render(request, "team/list.html")
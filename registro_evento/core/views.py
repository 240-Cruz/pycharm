from django.shortcuts import render
from .models import register


def index(request):
    template_name = "index.html"


    return render(request, template_name)





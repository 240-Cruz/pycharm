from django.shortcuts import render
from .models import register


def index(request):
    template_name="index.html"
    person = register.objects.all()
    return render(request, template_name)




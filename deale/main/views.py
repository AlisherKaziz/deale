from django.shortcuts import render
from .models import Company

# Create your views here.
def index(request):
    companies = Company.objects.all()

    return render(request, 'index.html', {'companies': companies})


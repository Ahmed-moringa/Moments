import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  index(request):
    # return HttpResponse('Welcome to Momments')
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'homepage.html')
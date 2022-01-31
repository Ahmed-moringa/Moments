import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  index(request):
    return HttpResponse('Welcome to Momments')

def homepage(request):
    html = f'''
            <html>
                <body>
                <h1>homepage</h1>
                </body>
            </html>
         '''
    return HttpResponse(html)
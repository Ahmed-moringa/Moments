import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    Image,
    Location,
)
# Create your views here.
def  index(request):
    # return HttpResponse('Welcome to Momments')
    images = Image.objects.all()
    locations = Location.get_locations()
    return render(request, 'index.html', {'images': images[::-1], 'locations': locations})

def image_location(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'location_images': images})

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search_results.html', {"message": message})
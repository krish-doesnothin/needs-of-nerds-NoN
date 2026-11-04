from django.shortcuts import render

def home(request):
    # The render function takes the request and the path to your HTML file
    return render(request, 'base/home.html')
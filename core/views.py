from django.shortcuts import render, redirect

def resources_view(request):
    return render(request, 'resource.html')
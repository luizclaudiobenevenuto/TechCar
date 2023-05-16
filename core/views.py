from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ios(request):
    return render(request, 'ios.html')

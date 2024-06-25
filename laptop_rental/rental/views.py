from django.shortcuts import render

def index(request):
    return render(request, 'rental/index.html')

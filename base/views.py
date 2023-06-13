from django.shortcuts import render,redirect

# Create your views here.

def indexpage(request):
    return render(request, 'layouts/main.html')

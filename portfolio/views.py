from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    return render(request, 'portfolio/homepage.html')

def career(request):
    return render(request, 'portfolio/career.html')

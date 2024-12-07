from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'attc_app/index.html')

def membership(request):
    return render(request, 'attc_app/membership.html')

def about(request):
    return render(request, 'attc_app/about.html')
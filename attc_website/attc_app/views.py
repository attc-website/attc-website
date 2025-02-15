from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'attc_app/index.html')

def membership(request):
    return render(request, 'attc_app/membership.html')

def about(request):
    return render(request, 'attc_app/about.html')

def facilities(request):
    return render(request, 'attc_app/facilities.html')

def coaching(request):
    return render(request, 'attc_app/coaching.html')

def leagues(request):
    return render(request, 'attc_app/leagues.html')

def news(request):
    return render(request, 'attc_app/news.html')

def contact(request):
    return render(request, 'attc_app/contact.html')

def gallery(request):
    return render(request, 'attc_app/gallery.html')
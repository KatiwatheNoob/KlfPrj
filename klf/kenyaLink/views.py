from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')

def permits(request):
    return render(request, 'permits.html')
def passes(request):
    return render(request, 'passes.html')
def visas(request):
    return render(request, 'visas.html')
def permanentresidency(request):
    return render(request, 'permanentresidency.html')
def citizenship(request):
    return render(request, 'citizenship.html')


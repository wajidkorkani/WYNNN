from django.shortcuts import render

# Create your views here.
def home(request):
    template = 'Core/home.html'
    return render(request, template)

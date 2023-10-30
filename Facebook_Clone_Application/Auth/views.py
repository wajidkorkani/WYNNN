from django.shortcuts import render

# Create your views here.
def login(request):
    template = 'Auth/login.html'
    context = {
        'text' : 'Hello world!'
    }
    return render(request, template, context)
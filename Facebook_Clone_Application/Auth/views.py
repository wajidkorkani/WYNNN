from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import get_user_model, login as login_user, logout as logout_user, authenticate
import random

# Create your views here.

def generate_otp():
    return str(random.randint(1000, 9999))

def Registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            request.session['signup_otp'] = generate_otp()
            request.session['signup_username'] = form.cleaned_data['username']
            request.session['signup_fname'] = form.cleaned_data['first_name']
            request.session['signup_lname'] = form.cleaned_data['last_name']
            request.session['signup_password'] = form.cleaned_data['password1']
            return redirect('verify_otp')
    else:
        form = RegistrationForm()
    template = 'Auth/signup.html'
    context = {'form':form}
    return render(request, template, context)


def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get("otp")
        expected_otp = request.session['signup_otp']
        if entered_otp == expected_otp:
            User = get_user_model()
            user = User.objects.create_user(
                username = request.session.get('signup_username'),
                first_name = request.session.get('signup_fname'),
                last_name = request.session.get('signup_lname'),
                password = request.session.get('signup_password')
            )
            user.save()
            return redirect('/')
        else:
            return render(request, 'auth/verify_otp.html', {'error_message': f"Please enter this OTP {otp}"})
    template = 'Auth/verify_otp.html'
    context = {'otp': request.session['signup_otp']}
    return render(request, template, context)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('/home/')
        else:
            return redirect('/')
    template = 'Auth/index.html'
    return render(request, template)

def user_logout_option(request):
    logout_user(request)
    return redirect('/')

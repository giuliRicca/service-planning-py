# apps/auth/views.py
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Import Custom forms
from apps.auth.forms import UserCreationForm 


def login_view(request):
    # return user to home page if already logged in
    if request.user.is_authenticated:
        return redirect("schedule")
    context = {}
    if request.method == 'POST':
        # Get email and password from post request
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if post reuqest values authenticate
        user = authenticate(request, username=email, password=password)
        if user:
            # If User Exists login with post request values
            login(request, user)
            return redirect("schedule")
        else:
            print("User Not found")

    return render(request, "auth/login.html", context)

def register_view(request):
    # return user to home page if already logged in
    if request.user.is_authenticated:
        return redirect('schedule')

    context = {}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Account Registered Successfully")
            return redirect('login')
        context['form'] = form
    else:
        context['form'] = UserCreationForm()

    return render(request, "auth/register.html", context)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    print('User logged out successfully')
    return redirect('login')

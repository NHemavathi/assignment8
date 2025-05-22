# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('home')  # redirect to homepage or dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

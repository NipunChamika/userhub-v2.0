from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('user_list')

    return render(request, 'user_create.html')

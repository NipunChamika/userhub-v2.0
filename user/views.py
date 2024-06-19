from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
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


def user_update(request, pk):
    form = UserForm()
    try:
        user = get_object_or_404(User, pk=pk)
    except Http404:
        messages.error(request, 'User does not exist.')
        return redirect('user_list')
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'user_update.html', {'form': form})

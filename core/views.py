from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import *
from .forms import *


def landing(request):
    context = {}
    return render(request, 'core/landing.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            usr = User.objects.get(username=form.cleaned_data['username'])
            Profile.objects.create(
                user = usr,
                address='Add an address!',
                phone='Add a phone number!'
            )
            messages.success(request, 'Your Account Was Created Successfully!')
            return redirect('core:login')
        
    else:
        form = SignupForm()
    context = {
        'form': form
    }
    return render(request, 'auth/signup.html', context)


@login_required
def index(request):
    context = {}
    return render(request, 'core/index.html', context)


@login_required
def LogoutView(request):
    logout(request)
    return redirect('core:login')


def about(request):
    context = {}
    return render(request, 'admission/about.html', context)


@login_required    
def settings(request):
    profile = Profile.objects.get(user=request.user)
    return render(
        request=request,
        template_name='auth/settings.html',
        context={
            'profile': profile
        }
    )


@login_required
def edit_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            x = form.save(commit=False)
            x.user = request.user
            x.save()
            return redirect('core:settings')
    else:
        form = EditProfileForm(instance=profile)
    return render(
        request=request,
        template_name="auth/edit_profile.html",
        context={
            'profile': profile,
            'form': form
        }
    )


@login_required
def users_detail(request, pk):
    users = get_object_or_404(Profile, pk=pk)
    return render(
        request=request,
        template_name='core/userdetails.html',
        context={
            'users': users,
        }
    )


def academics(request):
    context = {}
    return render(request, 'admission/academics.html', context)


def terms(request):
    context = {}
    return render(request, 'core/terms.html', context)


def privacy_policy(request):
    context = {}
    return render(request, 'core/privacy.html', context)
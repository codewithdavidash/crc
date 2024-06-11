from django.shortcuts import render, redirect


def gallery(request):
    context = {}
    return render(request, 'gallery/index.html', context)
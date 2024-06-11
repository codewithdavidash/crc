from django.shortcuts import render, redirect


def admission(request):
    context = {}
    return render(request, 'admission/index.html', context)

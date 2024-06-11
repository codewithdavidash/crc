from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import CommentForm, BlogForm
from django.contrib import messages
from core.models import Profile
from django.db.models import Q
from .models import (
    Comments,
    Blog,
)


@login_required
def blog(request):
    profile = Profile.objects.get(user=request.user)
    blog = Blog.objects.filter(status='available')
    context = {
        'i': profile,
        'blog': blog,
    }
    return render(request, 'blog/index.html', context)


@login_required
def favourites(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.favourites.filter(id=request.user.id).exists():
        blog.favourites.remove(request.user)
        messages.success(request, 'Blog Unsaved!')
    else:
        blog.favourites.add(request.user)
        messages.success(request, 'Blog Saved!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    

@login_required
def favourites_list(request):
    new = Blog.newmanager.filter(favourites=request.user)
        
    return render(request, 'blog/favourites_list.html', context={
        'new': new,
    })


@login_required
def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    fav = bool
    if blog.favourites.filter(id=request.user.id).exists():
        fav = True
    comment = Comments.objects.filter(blog=blog)
    com = Comments.objects.all()
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.sent_by = profile
            x.blog = blog
            x.save()
            return redirect('details', pk=pk)
    else:
        form = CommentForm()
    return render(
        request=request,
        template_name='blog/details.html',
        context={
            'comment': comment,
            'blog': blog,
            'form': form,
            'com': com,
            'fav': fav,
            'pk': pk,
        }
    )


@login_required
def add_blog(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False)
            x.created_by = profile
            x.save()
            messages.success(request, 'You posted a blog!')
            return redirect('blogs')
        
    else:
        form = BlogForm()
    
    context = {
        'form': form
    }
    return render(request, 'blog/add.html', context)


@login_required
def edit_blog(request, pk):
    profile = Profile.objects.get(user=request.user)
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            x = form.save(commit=False)
            x.created_by = profile
            x.save()
            messages.success(request, 'You edited the blog!')
            return redirect('blogs')
        
    else:
        form = BlogForm(instance=blog)
    
    context = {
        'form': form,
        'blog': blog
    }
    return render(request, 'blog/edit.html', context)


@login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('blogs')
    
    context = {
        'blog': blog
    }
    return render(request, 'blog/delete.html', context)


def search(request):
    query = request.GET.get('query', '')
    blog = Blog.objects.filter(status="available")
    
    if query:
        blog = blog.filter(Q(title__icontains=query)| Q(intro__icontains=query))
    
    return render(request, 'blog/search.html', context={
        'query': query,
        'blog': blog,
    })

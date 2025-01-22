from django.shortcuts import render,redirect
from .models import PostModel
from .forms import PostModelForm,PostUpdateForm

def index(request):
    
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()

    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'blogApp/index.html',context)

def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'blogApp/post_detail.html', context)

def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blogApp/post_edit.html', context)

def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post': post
    }
    return render(request, 'blogApp/post_delete.html', context)
    
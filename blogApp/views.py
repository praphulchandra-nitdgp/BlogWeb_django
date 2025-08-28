from django.shortcuts import render,redirect
from .models import PostModel, Comment
from .forms import PostModelForm,PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from .forms import ContactForm

@login_required
def index(request):
    
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
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

@login_required
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.post = post
            instance.author = request.user
            instance.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'c_form': c_form,
        'post': post,
    }
    return render(request, 'blogApp/post_detail.html', context)

@login_required
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
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

@login_required
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post': post
    }
    return render(request, 'blogApp/post_delete.html', context)
    
# About Page
def about_view(request):
    return render(request, 'blogApp/about.html')

# Contact Page
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('contact') 
    else:
        form = ContactForm()
    return render(request, 'blogApp/contact.html', {'form': form})
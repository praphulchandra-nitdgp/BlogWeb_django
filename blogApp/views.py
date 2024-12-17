from django.shortcuts import render,redirect
from .models import PostModel
from .forms import PostModelForm

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



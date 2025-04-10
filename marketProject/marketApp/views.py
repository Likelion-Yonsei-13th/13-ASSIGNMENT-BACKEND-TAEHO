from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html')

def post_create(request):

    if request.method == 'POST':
        price = request.POST.get('price')
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(price=price, title=title, content=content)
        return redirect('home')
    
    return render(request, 'create.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})

def product_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'product_detail.html', {
        'post': post
    })

def product_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.price = request.POST.get('price')
        post.save()
        return redirect('product_detail', pk=pk)
    return render(request, 'product_edit.html', {'post': post})

def product_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'product_delete.html', {'post': post})

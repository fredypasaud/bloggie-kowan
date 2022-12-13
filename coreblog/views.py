from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

@login_required
def create_blog(request):
    user = request.user
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = BlogPost.objects.create(
                author = user,
                judul_blog = form.cleaned_data.get('judul_blog'),
                blog_post = form.cleaned_data.get('blog_text'),
                post_time = datetime.now()
            )
            blog_post.save()
    return redirect("/")

@login_required
def delete_blog(request, id):
    if request.method == 'POST':
        blog_post = BlogPost.objects.filter(pk = id)
        blog_post.delete
    return redirect("/")

def see_all_post(request):
    blog_post = BlogPost.objects.all()
    context = {
        'list_blog': blog_post
    }
    return render(request, 'index.html', context)

def see_detailed_post(request, id_blog):
    blog_post = BlogPost.objects.get(pk = id_blog)
    context = {
    'blog_author' : blog_post.author.username,
    'blog_post': blog_post.blog_text,
    'post_title': blog_post.judul_blog,
    'post_time': blog_post.post_time}
    return render(request, 'post.html', context)

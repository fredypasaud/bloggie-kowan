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

def see_all_post_non_specific_user(request):
    blog_post = BlogPost.objects.all()
    for blog in blog_post:
        context = {
            'blog_author' : blog.author.get_username,
            'blog_post': blog.blog_text,
            'post_title': blog.judul_blog,
            'post_time': blog.post_time
        }
    return render(request, 'blog_post.html', context)

def see_all_post_specific_user(request, username):
    blog_post = BlogPost.objects.filter(author = username)
    for blog in blog_post:
        context = {
            'blog_author' : blog.author.get_username,
            'blog_post': blog.blog_text,
            'post_title': blog.judul_blog,
            'post_time': blog.post_time
        }
    return render(request, 'blog_post.html', context)

def see_detailed_post(request, id):
    blog_post = BlogPost.objects.filter(pk = id)
    context = {
    'blog_author' : blog_post.author.get_username,
    'blog_post': blog_post.blog_text,
    'post_title': blog_post.judul_blog,
    'post_time': blog_post.post_time}
    return render(request, 'blog_detailed.html', context)

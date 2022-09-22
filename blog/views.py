from django.shortcuts import render, get_list_or_404
from django.utils import timezone
from .models import Post
# Create your views here.

def index(request):
    # posts = Post.objects.filter(puslished_at__lte=timezone.now())
    posts = Post.objects.all()
    print("posts", posts)
    return render(request, "blog/index.html", {"posts" : posts})

def post_detail(request, slug):
    post = get_list_or_404(Post, slug=slug)
    print("post : ", post)
    return render(request, "blog/post-detail.html", {"post" : post[0]})
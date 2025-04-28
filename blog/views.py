
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import DetailView, ListView
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


class StartingPageView(ListView):
    template_name="blog/index.html"
    model=Post
    context_object_name="posts"
    ordering = ['-date']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name="blog/all-posts.html"
    model=Post
    context_object_name="all_posts"
    ordering = ['-date']

class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comments": post.comments.all().order_by('-id'),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
       
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comments": post.comments.all().order_by('-id'),
            "comment_form": comment_form
        }
        return render(request, "blog/post-detail.html", context)


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
        stored_posts = request.session.get('stored_posts') or []
        # isReadLater = request.session.get('post_slug') == slug
        isReadLater = slug in stored_posts
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comments": post.comments.all().order_by('-id'),
            "comment_form": CommentForm(),
            "isReadLater": isReadLater
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

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(slug__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        return render(request, "blog/stored-posts.html", context)
    

    def post(self, request):
        post_slug = request.POST['slug']
        stored_posts = request.session.get('stored_posts') or []
        if post_slug not in stored_posts:
            stored_posts.append(post_slug)
        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect(reverse("post-detail-page", args=[post_slug]))
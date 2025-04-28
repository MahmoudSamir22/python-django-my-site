
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import DetailView, ListView
from .forms import CommentForm

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

class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        context['comment_form'] = CommentForm()
        return context

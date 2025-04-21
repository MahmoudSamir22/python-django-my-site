from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

# Create your views here.

image_placeholder = "https://placehold.co/600x400"

posts = [
    {
        "slug": "intro-to-python",
        "title": "Getting Started with Python",
        "image": "https://placehold.co/600x400/306998/ffffff",
        "description": "An introductory guide to Python programming for beginners."
    },
    {
        "slug": "javascript-basics",
        "title": "JavaScript Basics for Web Development",
        "image": "https://placehold.co/600x400/f0db4f/323330",
        "description": "Learn the core concepts of JavaScript and how it's used in web development."
    },
    {
        "slug": "data-structures-in-cpp",
        "title": "Mastering Data Structures in C++",
        "image": "https://placehold.co/600x400/00427e/ffffff",
        "description": "A deep dive into data structures using the C++ programming language."
    },
    {
        "slug": "building-apis-with-node",
        "title": "Building RESTful APIs with Node.js",
        "image": "https://placehold.co/600x400/3c873a/ffffff",
        "description": "Learn how to create and manage RESTful APIs using Node.js and Express."
    },
    {
        "slug": "intro-to-react",
        "title": "Introduction to React.js",
        "image": "https://placehold.co/600x400/61dafb/20232a",
        "description": "A beginner's guide to building dynamic user interfaces with React.js."
    },
    {
        "slug": "python-data-analysis",
        "title": "Data Analysis with Python and Pandas",
        "image": "https://placehold.co/600x400/4584b6/ffffff",
        "description": "Explore how to analyze and visualize data using Python libraries like Pandas and Matplotlib."
    },
    {
        "slug": "docker-for-devs",
        "title": "Docker Essentials for Developers",
        "image": "https://placehold.co/600x400/0db7ed/ffffff",
        "description": "Learn the fundamentals of Docker and how to containerize your applications."
    },
    {
        "slug": "debugging-tips",
        "title": "Top Debugging Tips for Programmers",
        "image": "https://placehold.co/600x400/e44d26/ffffff",
        "description": "Improve your debugging skills with these practical tips and techniques."
    },
    {
        "slug": "clean-code-principles",
        "title": "Writing Clean and Maintainable Code",
        "image": "https://placehold.co/600x400/222831/f4f4f4",
        "description": "Discover the principles of clean code and how to apply them in your projects."
    },
    {
        "slug": "intro-to-git",
        "title": "Version Control with Git",
        "image": "https://placehold.co/600x400/f1502f/ffffff",
        "description": "A step-by-step guide to using Git for version control and collaboration."
    }
]



def index(request):
    return render(request,'blog/index.html')

def postBySlug(request, slug):
    existedPost = None
    for post in posts:
        if post["slug"] == slug:
            existedPost = post
            break
    
    if existedPost:
        return render(request, "blog/post.html", existedPost)
    else:
        response = render_to_string("404.html")
        return HttpResponseNotFound(response)
    
def getPosts(request):
    return render(request, "blog/allPosts.html", {
        "posts": posts,
    })
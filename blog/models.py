from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=30)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length= 80)
    excerpt = models.CharField(max_length= 500)
    image = models.CharField(max_length= 80)
    date = models.DateField()
    slug = models.SlugField()
    content = models.CharField(max_length= 500)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag)
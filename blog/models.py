from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length= 80)
    excerpt = models.CharField(max_length= 500)
    image = models.ImageField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True, db_index=True, unique= True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,null=True, on_delete = models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name='posts')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
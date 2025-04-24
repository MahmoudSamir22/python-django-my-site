from django.db import models
from django.utils.text import slugify

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
    image = models.CharField(max_length= 80)
    date = models.DateField()
    slug = models.SlugField(blank=True)
    content = models.CharField(max_length= 500)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
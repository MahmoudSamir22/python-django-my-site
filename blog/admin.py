from django.contrib import admin
from blog.models import Author, Post, Tag, Comment
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "caption",)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email")

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "excerpt", "image", "date", "slug", "content", "author",)
    prepopulated_fields = {"slug": ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "user_email", "text")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
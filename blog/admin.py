from django.contrib import admin
from blog.models import Author, Post, Tag
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "caption",)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email")

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "excerpt", "image", "date", "slug", "content", "author",)
    prepopulated_fields = {"slug": ('title',)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
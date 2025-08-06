from django.contrib import admin
from .models import Category, Post, Tag, Comment, Rating
# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Rating)


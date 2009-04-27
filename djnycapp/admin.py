from django.contrib import admin
from djnycapp.models import Post
from djnycapp.forms import PostForm

class PostAdmin(admin.ModelAdmin):
   form=PostForm

admin.site.register(Post, PostAdmin)

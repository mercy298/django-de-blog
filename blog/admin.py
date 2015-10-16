from django.contrib import admin
from .models import Post

# Register your models here.

# Postをadminページに登録する
admin.site.register(Post)

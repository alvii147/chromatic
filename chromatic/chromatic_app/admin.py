from django.contrib import admin

from .models import Post, Face

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Face)
class FaceAdmin(admin.ModelAdmin):
    pass
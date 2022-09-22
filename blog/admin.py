from django.contrib import admin

# Register your models here.
from .models import Tag, Post

admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    list_display = ("title", "puslished_at")
    

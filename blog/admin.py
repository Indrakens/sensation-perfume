from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin for blog """
    list_display = ('title', 'status', 'created_on') 
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on') 

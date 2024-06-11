from .models import Blog, Comments
from django.contrib import admin


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at']
    search_fields = ['title', 'created_by']

    
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['text', 'sent_by', 'sent_at']
    search_fields = ['text', 'sent_by']
    
    
    
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Blog, BlogAdmin)

from django.contrib import admin
from .models import Connection, Post, Comment

class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'connection', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__email', 'connection__email')

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'is_company_post')
    list_filter = ('is_company_post', 'created_at')
    search_fields = ('user__email', 'content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    search_fields = ('user__email', 'content')

admin.site.register(Connection, ConnectionAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

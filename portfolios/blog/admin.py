from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('create_at',)  # ✅ Исправлено

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'comments_count', 'share_count')
    list_filter = ('categories', 'tags')  # ✅ Исправлено
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

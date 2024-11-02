from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Book, CommentModel, TypeBook
from .models import CustomUser

# Register your models here.

admin.site.register(TypeBook)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name_book', 'author_book', 'book_file', 'slug')
    list_filter = ('author_book',)
    list_display_links = ('name_book', 'slug')
    prepopulated_fields = {'slug': ('name_book', 'author_book')}


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('user', 'post')




class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "username", 'subscribe', 'name', 'surname', 'type_user']
    list_filter = ['type_user']


CustomUserA = get_user_model()

admin.site.register(CustomUserA, CustomUserAdmin)
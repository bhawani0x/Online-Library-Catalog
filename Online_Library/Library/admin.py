from django.contrib import admin
from .models import Books, Author, Members

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'genre', 'publication', 'total_copies', 'available_copies')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'name', 'dob', 'nationality')
    filter_horizontal = ('books',)

@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'name', 'dob', 'doj')
    filter_horizontal = ('books',)

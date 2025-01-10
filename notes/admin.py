from django.contrib import admin
from .models import Note  # Import the Note model

# Register your models here.
@admin.register(Note)  # Use the decorator to register the model
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')  # Display these fields in the admin list view
    search_fields = ('title', 'text')  # Add search functionality for title and text

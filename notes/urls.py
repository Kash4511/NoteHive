from django.urls import path
from .views import notes_list_view, create_note_view, delete_note_view

urlpatterns = [
    path('list/', notes_list_view, name='notes_list'),
    path('new/', create_note_view, name='create_note'),
    path('delete/<int:note_id>/', delete_note_view, name='delete_note'),
]

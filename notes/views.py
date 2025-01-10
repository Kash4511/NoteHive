from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def notes_list_view(request):
    notes = Note.objects.filter(user=request.user)  # Fetch notes for the logged-in user
    return render(request, 'notes_list.html', {'notes': notes})


@login_required
def create_note_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        Note.objects.create(user=request.user, title=title, text=text)  # Save the note for the logged-in user
        return redirect('notes_list')  # Redirect to the notes list view

    return render(request, 'create_note.html')

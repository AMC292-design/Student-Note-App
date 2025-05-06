from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

@login_required
def dashboard(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/dashboard.html', {'notes': notes})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)  # Handle POST data
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Associate the note with the logged-in user
            note.save()
            return redirect('dashboard')  # Redirect after saving the note
    else:
        form = NoteForm()  # Initialize an empty form for GET requests

    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('dashboard')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})

from django.shortcuts import render

# Create your views here.

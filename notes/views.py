from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import NotesCreationForm
from django.contrib.auth.decorators import login_required
from .models import Note
# Create your views here.

class CreateNote(CreateView):
    form_class = NotesCreationForm
    success_url = reverse_lazy('home')
    template_name = 'notes/new_note.html'

    def form_valid(self, form):
        self.instance = form.save(commit=False)
        form.instance.user = self.request.user
        self.instance.save()
        return super().form_valid(form)

class NotesList(ListView):
    model = Note
    template_name = 'notes/notes_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user = self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class NoteDetail(DetailView):
    model = Note
    template_name='notes/notes_detail.html'

class NoteUpdate(UpdateView):
    model = Note
    template_name_suffix='_update'
    fields = ('title', 'content')

    def get_success_url(self):
        return reverse('notes:note_detail', args=(self.object.pk,))

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes:notes_list')
    template_name_suffix='_confirm_delete'

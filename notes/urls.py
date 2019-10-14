from django.urls import path
from . import views, models
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
app_name = 'notes'

urlpatterns = [
    path('new/', login_required(views.CreateNote.as_view()), name='new_note'),
    path('', login_required(views.NotesList.as_view()), name='notes_list'),
    path('<int:pk>/', login_required(views.NoteDetail.as_view()), name='note_detail'),
    path('<int:pk>/update/', login_required(views.NoteUpdate.as_view()), name='note_update'),
    path('<int:pk>/delete/', login_required(views.NoteDelete.as_view()), name='note_delete'),
    # path('delete/confirm/', login_required(TemplateView.as_view(template_name='notes/confirm_delete.html')),
    #     name='confirm_delete'),
]

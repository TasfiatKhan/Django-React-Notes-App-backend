from django.urls import path
from .views import NoteList, NoteDetail

app_name = 'notes_api'

urlpatterns = [
    path('<int:pk>/', NoteDetail.as_view(), name='detailcreate'),
    path('', NoteList.as_view(), name='listcreate'),
]

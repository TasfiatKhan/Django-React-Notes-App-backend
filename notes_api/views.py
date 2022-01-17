from rest_framework import generics
from note.models import Note
from .serializers import NoteSerializer

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    pass

class NoteDetail(generics.RetrieveDestroyAPIView):
    pass
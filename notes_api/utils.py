from rest_framework.response import Response
from note.models import Note, Tag
from .serializers import NoteSerializer
from users.models import User

def getNotesList(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def getNoteDetail(request, pk):
    user = request.user
    notes = user.note_set.all()
    note = notes.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

def createNote(request):
    user = request.user
    data = request.data
    note = Note.objects.create(
        body = data['body'],       
        author=user
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

def updateNote(request, pk):
    data = request.data
    user = request.user
    notes = user.note_set.all()
    note = notes.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteNote(request, pk):
    user = request.user
    notes = user.note_set.all()
    note = notes.get(id=pk)
    note.delete()
    return Response('Note was deleted!')
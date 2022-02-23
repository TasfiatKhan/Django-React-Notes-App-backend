from rest_framework import serializers
from note.models import Note, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class NoteSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Note
        fields = '__all__'
        
        

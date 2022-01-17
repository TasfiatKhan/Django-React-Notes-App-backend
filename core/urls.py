from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note.urls', namespace='note')),
    path('api/', include('notes_api.urls', namespace='notes_api')),    
]

from django.urls import path, include
from . import views
from .views import MyTokenObtainPairView
#from .views import NoteList, NoteDetail

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


app_name = 'notes_api'

urlpatterns = [
    #path('<int:pk>/', NoteDetail.as_view(), name='detailcreate'),
    #path('', NoteList.as_view(), name='listcreate'),
    
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]

from django.urls import path
from django.views.generic import TemplateView

app_name = 'note'

urlpatterns = [
    path('', TemplateView.as_view(template_name="note/index.html")),
]

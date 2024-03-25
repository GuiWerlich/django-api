from django.urls import path
from .views import MusicianView, MusicianDetailView

urlpatterns = [
    path("musicians/", MusicianView.as_view()),
    path("musicians/<int:pk>/", MusicianDetailView.as_view())
]
from django.urls import path, include
from .views import song_list, song_detail

urlpatterns = [
    path('', song_list, name='song_list'),
    path('<int:song_id>/', song_detail, name='song_detail'),
]
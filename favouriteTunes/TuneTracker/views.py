from django.shortcuts import render
from django.http import HttpResponseServerError

# Create your views here.
from .models import Song, Artist


def song_list(request):
    songs = Song.objects.all()

    return render(request, 'song_list.html', {'songs': songs})


def song_detail(request, song_id):
    try:
        song = Song.objects.get(id=song_id)
        return render(request, 'song_detail.html', {'song': song})
    except:
        return HttpResponseServerError(f"An error occurred")

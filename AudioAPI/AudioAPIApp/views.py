from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *

# Create your views here.

class AudioView(APIView):

    def get(self,request):

        song_obj = Song.objects.all()
        song_serial = SongSerializer(song_obj , many=True)

        podcast_obj = Podcast.objects.all()
        podcast_serial = PodcastSerializer(podcast_obj , many=True)

        audiobook_obj = AudioBook.objects.all()
        audiobook_serial = AudioBookSerializer(audiobook_obj , many=True)

        return Response({'song': song_serial.data , 'podcast': podcast_serial.data ,'audiobook': audiobook_serial.data})


    def post(self , request):
        song_serial = SongSerializer(data=request.data)
        podcast_serial = PodcastSerializer(data=request.data)
        audiobook_serial = AudioBookSerializer(data=request.data)

        if song_serial.is_valid() and podcast_serial.is_valid() and audiobook_serial.is_valid():
            song_serial.save()
            podcast_serial.save()
            audiobook_serial.save()
            return Response({'song': song_serial.data , 'podcast': podcast_serial.data ,'audiobook': audiobook_serial.data})
        return Response(song_serial.error , status= HTTP_400_BAD_REQUEST)


    def delete(self,  request, pk , format=None):
        song_obj = Song.objects.get(id=pk).delete()
        podcast_obj = Podcast.objects.get(id=pk).delete()
        audiobook_obj = AudioBook.objects.get(id=pk).delete()
        return Response(status.HTTP_204_NO_CONTENT)
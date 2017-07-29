from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from . models import Artist, Album, Song

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    model = Artist

    def get_queryset(self):
        return Artist.objects.all().order_by('name')

class DetailView(generic.DetailView):
    model = Artist
    template_name = 'music/detail.html'

    def get_queryset(self):
        '''excludes any questions that aren't published yet'''
        return Artist.objects.all()

def show_songs(request, album_name_slug):
    context_dict = {}

    try:
        #Can we find a category name slug with the given name?
        #If we can't the .get() method raises a DoesNotExist exception
        #So the .get() method returns one model instance or raises an exception
        album = Album.objects.get(slug=album_name_slug)

        #Retrieve all of the associated pages
        #Note that filter() will return a list of page objects or an empty list
        songs = Song.objects.filter(album=album)

        #Adds our results list ot the template context under name pages.
        context_dict['songs'] = songs
        #we also add the category object from
        #the database to the context dictionary
        #We'll use this in the template to verify that the category exists
        context_dict['album'] = album
    except Album.DoesNotExist:
        #we get here if we didnt find the specified category
        #dont do anything
        #the template will display the "no category" message for us.
        context_dict['album'] = None
        context_dict['songs'] = None

    #Go render the response and return it to the client
    return render(request, 'music/songs.html', context_dict)

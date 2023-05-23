from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Directores, Pelicula


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    peliculas = Pelicula.objects.all().count()

    # The 'all()' is implied by default.
    directores = Directores.objects.count()

    context = {
        'peliculas': peliculas,
        'directores': directores
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class pelicula_list(generic.ListView):
    model = Pelicula

class directores_list(generic.ListView):
    model = Directores

class PeliculaDetailView(generic.DetailView):
    model = Pelicula


def pelicula_detail_view(request, primary_key):
    pelicula = get_object_or_404(Pelicula, pk=primary_key)
    return render(request, 'catalog/pelicula_detail.html', context={'pelicula': pelicula})


class DirectoresDetailView(generic.DetailView):
    model = Directores


def directores_detail_view(request, primary_key):
    directores = get_object_or_404(Directores, pk=primary_key)
    return render(request, 'catalog/directores_detail.html', context={'directores': directores})

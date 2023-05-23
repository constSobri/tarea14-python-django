from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique book instances
from cine import settings


# Create your models here.
class Genero(models.Model):
    """Model representing a book genre."""
    genero = models.CharField(max_length=200, help_text='Agrega generos de peliculas.')

    def __str__(self):
        """String for representing the Model object."""
        return self.genero


class Pelicula(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Identificador unico.')

    titulo = models.CharField(max_length=200)

    director = models.ForeignKey('Directores', on_delete=models.SET_NULL, null=True)

    sipnosis = models.TextField(max_length=1000, help_text='Describe un poco sobre la peliculas sin mucho spoiler :)')

    fecha_de_estreno = models.DateField(null=True, blank=True)

    genero = models.ManyToManyField(Genero, help_text='Selecciona el genero de la pelicula.')

    portada = models.ImageField(upload_to=settings.MEDIA_URL)

    def __str__(self):
        """String for representing the Model object."""
        return self.titulo

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('detalles-pelicula', args=[str(self.id)])


class Directores(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Identificador unico.')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    peliculas = models.ManyToManyField('Pelicula', blank=True)

    class Meta:
        ordering = ['apellido', 'nombre']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('directores-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.apellido}, {self.nombre}'

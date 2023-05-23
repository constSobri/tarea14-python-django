from django.urls import path, include
from cine import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('peliculas/', views.pelicula_list.as_view(), name='peliculas'),
    path('peliculas/<uuid:pk>', views.PeliculaDetailView.as_view(), name='detalles-pelicula'),
    path('directores/<uuid:pk>', views.DirectoresDetailView.as_view(), name='directores-detail'),
    path('directores_list/', views.directores_list.as_view(), name='directores_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


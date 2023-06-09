# Generated by Django 4.1.9 on 2023-05-19 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_premio_remove_book_genre_delete_genre_book_premios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(help_text='Agrega generos de peliculas.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('sipnosis', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('fecha_de_estreno', models.DateField(blank=True, null=True)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author')),
                ('genero', models.ManyToManyField(help_text='Selecciona el genero de la pelicula.', to='catalog.genero')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='Premios',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Premio',
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.pelicula'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]

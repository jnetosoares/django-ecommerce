from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField('nome',max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name']
        db_tablespace = "categorias"

    def get_absolute_url(self):
        return reverse('catalogo:categoria', kwargs={'slug':self.slug})


class Product(models.Model):
    name = models.CharField('nome',max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('catolog.Category', verbose_name='Categoria')
    descrition = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço',decimal_places=2,max_digits=8)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('catalogo:produto', kwargs={'slug':self.slug})
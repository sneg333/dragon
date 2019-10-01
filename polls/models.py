from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Dom(models.Model):
    dom_title = models.CharField(max_length=200, verbose_name='заголовок')
    big_text= RichTextUploadingField(verbose_name='главный большой текст')

    class Meta:
        verbose_name = 'дом'
        verbose_name_plural = 'дом'

    def __str__(self):
        return self.dom_title

class Usluga(models.Model):
    title_usluga = models.CharField(max_length=200, verbose_name='услуга')
    title2_usluga = models.CharField(blank=True, max_length=200, verbose_name='услуга')
    body_usluga = RichTextUploadingField(blank=True, default='', verbose_name='услуга')
    body2_usluga = RichTextUploadingField(blank=True, default='', verbose_name='услуга')
    #image_usluga = models.ManyToManyField(Gallery, blank=True, verbose_name='фото услуги')

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуга'

    def __str__(self):
        return self.title_usluga

class Garantija(models.Model):
    title_garantija = models.CharField(max_length=200, verbose_name='гарантия')
    body_garantija = RichTextUploadingField(blank=True, default='', verbose_name='гарантия')
    body2_garantija = RichTextUploadingField(blank=True, default='', verbose_name='гарантия')
    is_active = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'гарантия'
        verbose_name_plural = 'гарантия'

    def __str__(self):
        return self.title_garantija

class Contact(models.Model):
    title_contact = models.CharField(max_length=200, verbose_name='контакт')
    body_contact = RichTextUploadingField(blank=True, default='', verbose_name='текст')
    adress_one_contact = RichTextUploadingField(blank=True, default='', verbose_name='первый адрес')
    adress_toe_contact = RichTextUploadingField(blank=True, default='', verbose_name='второй адрес')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакт'

    def __str__(self):
        return self.title_contact

class Dost_Oplat(models.Model):
    title_dostiop = models.CharField(max_length=200, verbose_name='доставка_и_оплата')
    body_dostiop = RichTextUploadingField(blank=True, default='', verbose_name='текст')

    class Meta:
        verbose_name = 'доставка_и_оплата'
        verbose_name_plural = 'доставка_и_оплата'

    def __str__(self):
        return self.title_dostiop

class Zakaz(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField()
    body_zakaz = models.CharField(max_length=400, verbose_name='текст')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    comment = RichTextUploadingField(blank=True, default='', verbose_name='комментарий')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Tovar(models.Model):
    slugt = models.SlugField('slugt', blank=True)
    title_tovar = models.CharField(max_length=400, verbose_name='Товар')
    image_start = models.ImageField(upload_to='tovar', blank=True)
    body_tovar = RichTextUploadingField(blank=True, default='', verbose_name='текст')
    #cena2 = models.CharField(max_length=200, blank=True, verbose_name='цена')
    cena = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='цена2')
    iden = models.DecimalField(max_digits=10, decimal_places=0, blank=True, verbose_name='артикль')
    body2_tovar = RichTextUploadingField(blank=True, default='', verbose_name='текст2')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товар'

    def __str__(self):
        return "%s, %s" % (self.cena, self.title_tovar)

class Gallery(models.Model):
    title_gallery = models.ForeignKey(Tovar, blank=True)
    photo_gallery = models.ImageField(upload_to='gallery', verbose_name='vse_gallery', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('title_gallery',)
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотогаллерея'

    def __str__(self):
        return "%s" % self.id

class PodKatalog(models.Model):
    title_podkatalog = models.CharField(max_length=200, verbose_name='подкаталог')
    slug = models.SlugField('slug')
    tovar_podkatalog = models.ManyToManyField(Tovar, verbose_name='товар')
    image_podkatalog = models.ImageField(upload_to='podkatalog', blank=True)

    class Meta:
        verbose_name = 'подкаталог'
        verbose_name_plural = 'подкаталог'

    def __str__(self):
        return self.title_podkatalog

class Katalog(models.Model):
    title_katalog = models.CharField(max_length=200, verbose_name='каталог')
    slug = models.SlugField('slug')
    podkatalog_katalog = models.ManyToManyField(PodKatalog, verbose_name='подкаталог', blank=True)

    class Meta:
        verbose_name = 'каталог'
        verbose_name_plural = 'каталог'

    def __str__(self):
        return self.title_katalog
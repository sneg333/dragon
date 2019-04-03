from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Dom(models.Model):
    dom_title = models.CharField(max_length=200, verbose_name='заголовок')
    big_text= models.TextField(max_length=200, verbose_name='главный большой текст')

    class Meta:
        verbose_name = 'дом'
        verbose_name_plural = 'дом'

    def __str__(self):
        return self.dom_title

class Gallery(models.Model):
    title_gallery = models.CharField(max_length=150, blank=True)
    photo_gallery = models.ImageField(upload_to='gallery', verbose_name='vse_gallery', blank=True)

    class Meta:
        ordering = ('title_gallery',)
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотогаллерея'

    def __str__(self):
        return self.title_gallery

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

class Tovar(models.Model):
    title_tovar = models.CharField(max_length=400, verbose_name='товар')
    body_tovar = RichTextUploadingField(blank=True, default='', verbose_name='текст')
    cena = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='цена')
    body2_tovar = RichTextUploadingField(blank=True, default='', verbose_name='текст2')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товар'

    def __str__(self):
        return self.title_tovar
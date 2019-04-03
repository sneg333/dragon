from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse


def home(request):
    dom = Dom.objects.all()

    context = {
        'dom':dom,
    }
    return render(request,'polls/home.html', context)


def contact(request):
    contact = Contact.objects.all()

    context = {
        'contact':contact,
        }
    return render(request,'polls/contact.html', context)

def dostiop(request):
    dostiop = Dost_Oplat.objects.all()

    context = {
        'dostiop':dostiop,
    }
    return render(request, 'polls/dostiop.html', context)

def usluga(request):
    usluga = Usluga.objects.all()

    context = {
        'usluga': usluga,
    }
    return render(request, 'polls/usluga.html', context)

def garantija(request):
    garantija = Garantija.objects.all()

    context = {
        'garantija': garantija,
    }
    return render(request, 'polls/garantija.html', context)
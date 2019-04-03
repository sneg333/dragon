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

from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import ZakazCreateForm
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    dom = Dom.objects.all()

    context = {
        'dom':dom,
    }
    return render(request,'polls/home.html', context)

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

def usluga_detail(request, usluga_id):
    usluga_detail = get_object_or_404(Usluga, pk = usluga_id)

    context = {
        'usluga_detail': usluga_detail,
    }
    return render(request, 'polls/usluga_detail.html', context)

def garantija(request):
    garantija = Garantija.objects.all()

    context = {
        'garantija': garantija,
    }
    return render(request, 'polls/garantija.html', context)

def contact(request):
    contact = Contact.objects.all()
    zakaz = Zakaz.objects.all()
    form = ZakazCreateForm(request.POST or None)

    if request.method == "POST":
        form = ZakazCreateForm(request.POST)
        if form.is_valid():
            post = Zakaz()
            post.first_name = form.cleaned_data['first_name']
            post.email = form.cleaned_data['email']
            post.body_zakaz = form.cleaned_data['body_zakaz']
            post.save()
            return HttpResponseRedirect(reverse('contactyes'))
        else:
            form = ZakazCreateForm()
    context = {
        'contact':contact,
        'zakaz': zakaz,
        'form': form,
        }
    return render(request,'polls/contact.html', context)

def contactyes(request):
    contact = Contact.objects.all()
    context = {
        'contact': contact,
    }
    return render(request, 'polls/contactyes.html', context)

def tovar(request):
    tovar = Tovar.objects.all()
    context = {
        'tovar': tovar,
    }
    return render(request, 'polls/tovar.html', context)

def tovar_detail(request, tovar_id):
    tovar_detail = get_object_or_404(Tovar, pk = tovar_id)

    context = {
        'tovar_detail': tovar_detail,
    }
    return render(request, 'polls/tovar_detail.html', context)
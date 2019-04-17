from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import ZakazCreateForm
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    dom = Dom.objects.all()
    usluga = Usluga.objects.all()
    katalog = Katalog.objects.all()

    context = {
        'dom':dom,
        'usluga': usluga,
        'katalog': katalog,
    }
    return render(request,'polls/home.html', context)

def podkatalog(request, slug):
    katalog = Katalog.objects.all()
    podkatalog = PodKatalog.objects.get(slug=slug)
    usluga = Usluga.objects.all()

    context = {
        'katalog':katalog,
        'podkatalog': podkatalog,
        'usluga': usluga,

    }
    return render(request, 'polls/podkatalog.html', context)

def tovar_detail(request, tovar_id):
    usluga = Usluga.objects.all()
    katalog = Katalog.objects.all()
    tovar_detail = get_object_or_404(Tovar, pk = tovar_id)

    context = {
        'tovar_detail': tovar_detail,
        'usluga': usluga,
        'katalog': katalog,
    }
    return render(request, 'polls/tovar_detail.html', context)

def katalog_one(request, slug):
    katalog_one = Katalog.objects.get(slug=slug)
    katalog = Katalog.objects.all()
    podkatalog = PodKatalog.objects.all()
    usluga = Usluga.objects.all()

    context = {
        'katalog_one': katalog_one,
        'katalog': katalog,
        'podkatalog': podkatalog,
        'usluga': usluga,
    }
    return render(request, 'polls/katalog_one.html', context)

def dostiop(request):
    katalog = Katalog.objects.all()
    dostiop = Dost_Oplat.objects.all()
    usluga = Usluga.objects.all()

    context = {
        'dostiop':dostiop,
        'katalog': katalog,
        'usluga': usluga,
    }
    return render(request, 'polls/dostiop.html', context)

def usluga(request):
    katalog = Katalog.objects.all()
    usluga = Usluga.objects.all()

    context = {
        'usluga': usluga,
        'katalog':katalog,
    }
    return render(request, 'polls/usluga.html', context)

def usluga_detail(request, usluga_id):
    katalog = Katalog.objects.all()
    usluga_detail = get_object_or_404(Usluga, pk = usluga_id)
    usluga = Usluga.objects.all()

    context = {
        'usluga_detail': usluga_detail,
        'katalog': katalog,
        'usluga': usluga,
    }
    return render(request, 'polls/usluga_detail.html', context)

def garantija(request):
    garantija = Garantija.objects.all()
    katalog = Katalog.objects.all()
    usluga = Usluga.objects.all()

    context = {
        'garantija': garantija,
        'usluga': usluga,
        'katalog': katalog,
    }
    return render(request, 'polls/garantija.html', context)

def contact(request):
    contact = Contact.objects.all()
    katalog = Katalog.objects.all()
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
        'katalog': katalog,
        }
    return render(request,'polls/contact.html', context)

def contactyes(request):
    contact = Contact.objects.all()
    katalog = Katalog.objects.all()

    context = {
        'contact': contact,
        'katalog': katalog,
    }
    return render(request, 'polls/contactyes.html', context)


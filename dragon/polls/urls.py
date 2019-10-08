from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^katalog/(?P<slug>[\w]+)/$', views.katalog_one, name='katalog_one'),
    url(r'^katalog/detail/(?P<slug>[\w]+)/$', views.podkatalog, name='podkatalog'),
    url(r'^katalog/detail/detail/(?P<tovar_id>[0-9]+)$', views.tovar_detail, name='tovar_detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contactyes/$', views.contactyes, name='contactyes'),
    url(r'^dostiop/$', views.dostiop, name='dostiop'),
    url(r'^usluga/$', views.usluga, name='usluga'),
    url(r'^usluga/(?P<usluga_id>[0-9]+)$', views.usluga_detail, name='usluga_detail'),
    url(r'^garantija/$', views.garantija, name='garantija'),
    url(r'^korzina/$', views.korzina, name='korzina'),
   # url(r'^tovar/$', views.tovar, name='tovar'),
    #url(r'^tovar/(?P<tovar_id>[0-9]+)$', views.tovar_detail, name='tovar_detail'),

]
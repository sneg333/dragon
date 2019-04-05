from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contactyes/$', views.contactyes, name='contactyes'),
    url(r'^dostiop/$', views.dostiop, name='dostiop'),
    url(r'^usluga/$', views.usluga, name='usluga'),
    url(r'^garantija/$', views.garantija, name='garantija'),
    url(r'^tovar/$', views.tovar, name='tovar'),
    url(r'^tovar/(?P<tovar_id>[0-9]+)$', views.tovar_detail, name='tovar_detail'),

]
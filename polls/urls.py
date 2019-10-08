from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^katalog/(?P<slug>[\w]+)/$', views.katalog_one, name='katalog_one'),
    url(r'^katalog/detail/(?P<slug>[\w]+)/$', views.podkatalog, name='podkatalog'),
<<<<<<< HEAD
    url(r'^katalog/detail/detail/(?P<slugt>[\w]+)$', views.tovar_detail, name='tovar_detail'),
=======
    url(r'^katalog/detail/detail/(?P<tovar_id>[0-9]+)$', views.tovar_detail, name='tovar_detail'),
>>>>>>> a67ad82c94aaefd5389dc039041a0b4105c59841
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contactyes/$', views.contactyes, name='contactyes'),
    url(r'^dostiop/$', views.dostiop, name='dostiop'),
    url(r'^usluga/$', views.usluga, name='usluga'),
    url(r'^usluga/(?P<usluga_id>[0-9]+)$', views.usluga_detail, name='usluga_detail'),
    url(r'^garantija/$', views.garantija, name='garantija'),
<<<<<<< HEAD
=======
    url(r'^korzina/$', views.korzina, name='korzina'),
>>>>>>> a67ad82c94aaefd5389dc039041a0b4105c59841
   # url(r'^tovar/$', views.tovar, name='tovar'),
    #url(r'^tovar/(?P<tovar_id>[0-9]+)$', views.tovar_detail, name='tovar_detail'),

]
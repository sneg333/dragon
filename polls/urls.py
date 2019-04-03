from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^dostiop/$', views.dostiop, name='dostiop'),
    url(r'^usluga/$', views.usluga, name='usluga'),
    url(r'^garantija/$', views.garantija, name='garantija'),

]
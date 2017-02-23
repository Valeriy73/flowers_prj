from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^item/$', views.item, name='item'),
    url(r'^item/(?P<pk>\d+)/$', views.item, name='item'),
    url(r'^all_bunche.html', views.all_bunche, name='all_bunche'),

    ]
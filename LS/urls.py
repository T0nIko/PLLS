from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^about/$', views.about, name='about'),
]

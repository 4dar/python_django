from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_gold/(?P<building_type>\w+)', views.process),
    url(r'^clear_gold', views.clear)
]

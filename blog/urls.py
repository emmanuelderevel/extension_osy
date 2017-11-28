from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index$', views.index, name='index'),
    url(r'test$', views.test, name='test'),
    url(r'test_string$', views.test_string, name='test_string'),
]

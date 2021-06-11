import django
from django.conf.urls import url
from django.urls import include
from .views import registration,verify,create
app_name='registration'

urlpatterns = [
    url(r'^$',registration,name="registration"),
    url(r'verify/',verify,name="verify"),
    url(r'create/',create,name="create"),
]
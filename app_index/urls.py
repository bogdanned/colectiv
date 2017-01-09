from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', IndexView, name='index'),
    url(r'^pricing/$', PricingView, name='pricing'),
    url(r'^accounts/profile/$', ProfileView, name='profile'),
]

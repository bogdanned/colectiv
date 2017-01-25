from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', IndexView, name='index'),
    url(r'^pricing-commute/$', PricingCommuteView, name='pricing-commute'),
    url(r'^pricing-taxi/$', PricingTaxiView, name='pricing-taxi'),
    url(r'^routes/$', RouteView, name='routes'),
    url(r'^get-email/$', getEmail, name='get-email'),
    url(r'^accounts/profile/$', ProfileView, name='profile'),
    url(r'^email/profile/$', EmailProfileView, name='email-profile'),
]

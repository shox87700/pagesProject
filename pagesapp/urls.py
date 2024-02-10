from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, LinksPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('links/', LinksPageView.as_view(), name='links')
]

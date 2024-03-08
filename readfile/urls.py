from . import views
from django.urls import path


urlpatterns = [
    #home page url
    path('', views.home, name='home'),
]

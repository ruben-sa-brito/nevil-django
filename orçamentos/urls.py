from django.urls import path
from . import views

app_name = 'orçamentos'

urlpatterns = [
    path('', views.home, name="home"),
]
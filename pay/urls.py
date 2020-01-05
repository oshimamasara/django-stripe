from django.urls import path
from . import views

app_name = 'pay'
urlpatterns = [
    path('', views.pay, name='pay'),
]
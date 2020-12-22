from django.conf.urls import url 
from django.urls import path
from .views import index, bien, contacter_agence, Login, Logout, register

app_name = 'immob'
urlpatterns = [
    path('', index, name='index'),
    url('biens', bien, name='biens'),
    url('contacter_agence', contacter_agence, name='contacter_agence'),
    url('Login', Login, name='Login'),
    url('Logout', Logout, name='Logout'),
    url('register', register, name='register'),
]
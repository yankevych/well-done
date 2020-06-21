from django.urls import path

from . import views

app_name = 'about_myself'
urlpatterns = [
    path('', views.index, name='about_myself'),

]

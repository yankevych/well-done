from django.urls import path

from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.det_gallery, name='det_gallery'),

]

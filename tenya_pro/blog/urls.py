from django.urls import path

from .views import BlogPostView, BlogDetailView

app_name = 'blog'
urlpatterns = [
    path('', BlogPostView.as_view(), name='blog_base'),
    path('<int:pk>/', BlogDetailView.as_view(), name='det_base'),


]

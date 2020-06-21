from .models import Blog
from django.views.generic import ListView, DetailView


class BlogPostView(ListView):
    model = Blog
    template_name = 'blog/blog_base.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/det_base.html'

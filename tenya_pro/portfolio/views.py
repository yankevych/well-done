from django.shortcuts import render
from .models import Portfolio, PostsImages


def index(request):
    port_list = Portfolio.objects.all()
    return render(request, 'portfolio/first.html', {'port_list': port_list})


def det_gallery(request, article_id):
    port_list_det = Portfolio.objects.get_queryset().filter(id=article_id)
    port_list_det_all = PostsImages.objects.get_queryset().filter(post_id=article_id)
    return render(request, 'portfolio/det_gallery_first.html', {'det_gallery': port_list_det,
                                                                'list_all': port_list_det_all})




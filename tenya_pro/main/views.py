from django.shortcuts import render

from portfolio.models import Portfolio, PostsImages


def index(request):
    port_list = Portfolio.objects.all()
    return render(request, 'main/first.html', {'port_list': port_list})

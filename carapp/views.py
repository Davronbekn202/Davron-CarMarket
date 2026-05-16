from django.shortcuts import render
from django.views.generic import ListView,TemplateView


class Base(TemplateView):
    template_name='base.html'


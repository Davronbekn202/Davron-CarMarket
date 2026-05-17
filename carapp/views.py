from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Car
from .forms import ProductForm
from django.urls import reverse_lazy


class CarBaseView(ListView):
    model = Car
    template_name = 'base.html'
    context_object_name = 'cars'


class CarDetail(DetailView):
    model = Car
    template_name = 'cars/detail.html'
    context_object_name = 'cars'
    pk_url_kwarg = 'pk'


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    form_class = ProductForm
    template_name = 'cars/create.html'
    success_url = reverse_lazy('carapp:base')

    def form_valid(self, form):
        form.instance.seller = self.request.user

        return super().form_valid(form)


class CarUpdate(UpdateView):
    model = Car
    form_class = ProductForm
    template_name = 'cars/update.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('carapp:base')


class CarDelete(DeleteView):
    model = Car
    template_name = 'cars/delete.html'
    success_url = reverse_lazy('carapp:base')

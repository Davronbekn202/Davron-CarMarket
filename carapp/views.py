from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Car, LocationOfProductModel
from .forms import ProductForm, LocationOfProductForm
from django.urls import reverse_lazy


class CarBaseView(TemplateView):
    model = Car
    template_name = 'main.html'


class CarsView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'


class CarDetail(DetailView):
    model = Car
    template_name = 'cars/detail.html'
    context_object_name = 'car'
    pk_url_kwarg = 'pk'


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    form_class = ProductForm
    template_name = 'cars/create.html'
    success_url = reverse_lazy('carapp:product-location-create')

    def form_valid(self, form):
        form.instance.seller = self.request.user

        return super().form_valid(form)


class CarUpdate(LoginRequiredMixin,UpdateView):
    model = Car
    form_class = ProductForm
    template_name = 'cars/update.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('carapp:product-location-update')


class CarDelete(LoginRequiredMixin,DeleteView):
    model = Car
    template_name = 'cars/delete.html'
    success_url = reverse_lazy('carapp:base')


# location
class LocationOfProductCreateView(LoginRequiredMixin, CreateView):
    model = LocationOfProductModel
    template_name = 'cars/location/create.html'
    form_class = LocationOfProductForm
    success_url = reverse_lazy('carapp:base')


class LocationOfProductUpdateView(LoginRequiredMixin, CreateView):
    model = LocationOfProductModel
    template_name = 'cars/location/update.html'
    form_class = LocationOfProductForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('carapp:base')

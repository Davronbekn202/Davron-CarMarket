from django.urls import path
from . import views

app_name = 'carapp'

urlpatterns = [
    path('',views.CarBaseView.as_view(), name='base'),
    path('cars/',views.CarsView.as_view(), name='cars'),
    path('car-create/',views.CarCreate.as_view(), name='car-create'),
    path('car-update/<int:pk>/',views.CarUpdate.as_view(), name='car-update'),
    path('car-detail/<int:pk>/',views.CarDetail.as_view(), name='car-detail'),
    path('car-delete/<int:pk>/',views.CarDelete.as_view(), name='car-delete'),

    #location
    path('product-location-create/',views.LocationOfProductCreateView.as_view(), name='product-location-create'),
    path('product-location-update/<int:pk>/',views.LocationOfProductUpdateView.as_view(), name='product-location-update'),
]

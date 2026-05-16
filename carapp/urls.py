from django.urls import path
from . import views

app_name = 'carapp'

urlpatterns = [
    path('',views.Base.as_view(), name='base')

]

from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'appliances'

urlpatterns = [
    path('brands/', views.brand_list_view, name="brand_list")
]

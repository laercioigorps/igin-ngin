from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'appliances'

urlpatterns = [
    path('brands/', views.brand_list_view, name="brand_list"),
    path('brands/<int:pk>/', views.brand_detail_view, name="brand_detail"),
    path('categories/', views.category_list_view, name="category_list"),
    path('categories/<int:pk>/', views.category_detail_view, name="category_detail"),
]

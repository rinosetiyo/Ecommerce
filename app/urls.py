from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('store/', views.store_page, name="store_page"),
    path('store/<slug:category_slug>/', views.store, name="store"),
    path('store/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name="product_detail"),
]
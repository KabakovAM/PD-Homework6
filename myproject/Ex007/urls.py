from django.urls import path
from . import views

urlpatterns = [
    path('good_update/', views.good_update, name='good_update'),
    path('good_image/', views.good_image, name='good_image'),
    path('client_orders_by_time/<int:client_id>/', views.client_orders_by_time, name='client_orders_by_time'),
    path('client_orders/<int:client_id>/', views.client_orders, name='client_orders'),
]
from django.urls import path
from . import views
from .views import order_page, customer_creation_page, order_list, update_order, delete_order

urlpatterns = [
     path('', views.home_page, name="Homepage" ),
     path('order/', views.order_page, name="orderpage" ),
     path('login/', views.login_page, name="loginpage" ),
     path('order/', order_page, name='ordering_page'),
     path('create/', customer_creation_page, name='customer_creation_page'),
     path('orders/', order_list, name='order_list'),
     path('update_order/<int:order_id>/', update_order, name='update_order'),
     path('delete_order/<int:order_id>/', delete_order, name='delete_order'),

]
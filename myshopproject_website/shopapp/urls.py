from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home"),
    path('registration', views.registration_page, name="registration"),
    path('login', views.login_page, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('contact', views.contact_page, name="contact"),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]
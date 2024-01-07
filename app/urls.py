from django.urls import path
from app import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    #for mobile html file
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    #for topwear html file
    path('topwear/',views.topwear,name='topwear'),
    path('topwear/<slug:data>',views.topwear,name='topweardata'),

    #for bottomwear html file
    path('bottomwear/',views.bottomwear,name='bottomwear'),
    path('bottomwear/<slug:data>',views.bottomwear,name='bottomweardata'),
    
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

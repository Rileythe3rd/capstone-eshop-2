from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    
	
	#Leave as empty string for base url
	path('', views.store, name="store"),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
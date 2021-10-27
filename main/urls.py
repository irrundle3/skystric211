from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
  path("", views.homepage, name="homepage"),
  path("register/", views.register, name="register"),
  path("inventory/", views.inventory, name="inventory"),
  path("design/", views.design, name="design"),
  path("contactus/", views.contactus, name="contactus"),
  path("login/", views.login_request, name="login"),
  path("logout/", views.logout_request, name="logout"),
  path("designdownloadeditor/", views.designdownloadeditor, name="designdownloadeditor"),
  path("designelectrical/", views.designelectrical, name="designelectrical"),
  path("designphysicalstructure/", views.designphysicalstructure, name="designphysicalstructure"),
  path("longproddesc/<product_title>", views.longproddesc, name='longproddesc'),
  path("cart/", views.cart, name='cart'),
  path("cart/<product_title>/", views.cartchg, name='cartchg'),
  path("deletecartitem/<product_title>", views.deletecartitem, name="deletecartitem"),
  path("checkout/", views.checkout, name="checkout"),
  path("addonetocart/<product_title>/", views.addonetocart, name="addonetocart"),
  path("constructor/", views.constructor, name="constructor"),
  path("inventory/<sort_id>/", views.inventorychg, name="inventorychg"),
]

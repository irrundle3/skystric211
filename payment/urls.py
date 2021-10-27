from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

app_name = "payment"

urlpatterns = [
    path("process", views.payment_process, name="process"),
    path("done", views.payment_done, name="done"),
    path("cancelled", views.payment_cancelled, name="cancelled"),
]

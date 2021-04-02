from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.productDetailView),
    path('create', views.productCreate),
]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myview/<int:id>', views.myView),
    path('product/', include('products.urls')),

]

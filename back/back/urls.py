from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', views.ProductListCreateView.as_view(), name='product-list-create'),  # 追加
    path('', views.index, name='index'),
]

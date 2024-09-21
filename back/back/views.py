from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse

# ルート用のビュー
def index(request):
    return HttpResponse("Hello, this is the homepage!")

# プロダクトのリストと作成用のビュー
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()  # 全プロダクトのクエリセット
    serializer_class = ProductSerializer  # シリアライザを指定

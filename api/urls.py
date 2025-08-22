from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet,CategoryViewSet

routers = SimpleRouter()
routers.register('products',ProductViewSet)
routers.register('categories',CategoryViewSet)

urlpatterns = routers.urls

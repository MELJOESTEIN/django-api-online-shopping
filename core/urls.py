from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop.views import (
    CategoryViewset, 
    ProductViewset, 
    ArticleViewset,
    AdminCategoryViewset
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create a router and register our viewsets
router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename='category')
router.register('admin/category', AdminCategoryViewset, basename='admin-category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')

# The API URLs are automatically determined by the router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
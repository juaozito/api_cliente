from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cliente.views import ClienteViewSet 

# Removido imports do Simple JWT (TokenObtainPairView, TokenRefreshView)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rotas da sua API (CRUD de Clientes)
    path('api/', include(router.urls)),
    
    # Rotas JWT removidas (path('api/token/', ...))
]
from rest_framework import viewsets
from rest_framework.permissions import AllowAny # <-- PERMISSÃO PÚBLICA AGORA
from .models import Cliente
from .serializers import ClienteSerializer

class BaseClienteViewSet(viewsets.ModelViewSet):
    """
    Define a interface básica para ViewSets de Cliente.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteViewSet(BaseClienteViewSet):
    """
    View principal: Permissão AllowAny para CRUD público.
    """
    # ⚠️ PERMISSÃO MODIFICADA: Desativa a autenticação JWT/Token
    permission_classes = [AllowAny] 
    
    # Exemplo de otimização de queryset (baixo acoplamento com o DB)
    queryset = Cliente.objects.all().select_related('endereco').order_by('nome') 

    # Polimorfismo: Opcional, se você quiser sobrescrever o método list
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
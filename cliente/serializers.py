from rest_framework import serializers
from .models import Endereco, Cliente
from .utils import validate_cpf_format # Importa a função de Coesão

# ----------------------------------------------------
# MIXINS (Interfaces e Encapsulamento de Validação)
# ----------------------------------------------------
class ClienteValidationMixin:
    """
    Encapsula a lógica de validação de negócios (ex: CPF).
    """
    def validate_cpf(self, value):
        
        # 1. Checa o Formato (Coesão: usa a função externa)
        if not validate_cpf_format(value):
            raise serializers.ValidationError("O CPF está no formato incorreto ou tem um número inválido de dígitos.")
        
        # 2. Checagem de Unicidade
        if Cliente.objects.filter(cpf=value).exists():
            # Permite o PUT/UPDATE sem erro se o CPF não for alterado
            if self.instance and self.instance.cpf == value:
                pass
            else:
                raise serializers.ValidationError("Este CPF já está cadastrado no sistema.")
        
        return value

# ----------------------------------------------------
# Serializador do Endereço
# ----------------------------------------------------
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'rua', 'numero', 'cep', 'bairro', 'cidade', 'uf')
        read_only_fields = ('id',)

# ----------------------------------------------------
# Serializador do Cliente
# ----------------------------------------------------
class ClienteSerializer(ClienteValidationMixin, serializers.ModelSerializer):
    endereco = EnderecoSerializer(required=True)

    class Meta:
        model = Cliente
        fields = ('id', 'cpf', 'nome', 'endereco') 
        read_only_fields = ('id',)

    # Método CREATE: Baixo Acoplamento na criação
    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco_instance = Endereco.objects.create(**endereco_data)
        
        cliente_instance = Cliente.objects.create(
            endereco=endereco_instance, 
            **validated_data
        )
        return cliente_instance

    # Método UPDATE: Baixo Acoplamento na atualização
    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('endereco', {})
        
        # 1. Atualiza Cliente
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # 2. Atualiza Endereco
        endereco_instance = instance.endereco
        for attr, value in endereco_data.items():
            setattr(endereco_instance, attr, value)
        
        endereco_instance.save()
        instance.save()
        return instance
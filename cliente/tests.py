# cliente/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Cliente, Endereco

class ClienteAPITest(APITestCase):
    
    def setUp(self):
        # Configuração inicial: URL base para a lista de clientes
        self.url_list = reverse('cliente-list') 
        
        # Dados de teste para criar um cliente
        self.cliente_data = {
            "cpf": "123.456.789-00",
            "nome": "Cliente Teste",
            "endereco": {
                "rua": "Rua da Paz",
                "numero": 123,
                "cep": "01000-000",
                "bairro": "Bairro Teste",
                "cidade": "Cidade Teste",
                "uf": "TS"
            }
        }

    # Teste para garantir que um cliente pode ser criado via POST
    def test_create_cliente(self):
        """Garante que a criação de um novo cliente funciona."""
        response = self.client.post(self.url_list, self.cliente_data, format='json')
        
        # Verifica se o status retornado é 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verifica se um novo objeto Cliente foi criado no banco de dados
        self.assertEqual(Cliente.objects.count(), 1)
        
        # Verifica se o Endereco aninhado também foi criado
        self.assertEqual(Endereco.objects.count(), 1)
        
        # Opcional: verifica se o nome está correto
        self.assertEqual(Cliente.objects.get().nome, 'Cliente Teste')

    # Teste para garantir que a listagem de clientes funciona
    def test_list_clientes(self):
        """Garante que a listagem de clientes funciona."""
        # Cria um cliente primeiro para garantir que a lista não está vazia
        self.client.post(self.url_list, self.cliente_data, format='json')
        
        # Faz a requisição GET para listar
        response = self.client.get(self.url_list, format='json')
        
        # Verifica se o status retornado é 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verifica se a lista retornada contém o cliente criado
        self.assertEqual(len(response.data), 1)

    # Você pode adicionar mais testes aqui para PUT, DELETE, validação de CPF, etc.
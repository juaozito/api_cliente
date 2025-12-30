from django.db import models

# ----------------------------------------------------
# ABSTRAÇÃO e HERANÇA: Classe Abstrata
# ----------------------------------------------------
class PessoaBase(models.Model):
    """
    Classe Abstrata para herdar campos comuns (cpf e nome).
    """
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    nome = models.CharField(max_length=100)

    class Meta:
        abstract = True # Não cria tabela no banco

# ----------------------------------------------------
# Endereco (Entidade separada)
# ----------------------------------------------------
class Endereco(models.Model):
    rua = models.CharField(max_length=150)
    numero = models.IntegerField()
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"

# ----------------------------------------------------
# Cliente (Herda de PessoaBase)
# ----------------------------------------------------
class Cliente(PessoaBase): 
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # ESTA LINHA É CRUCIAL: 'api_cliente' deve ser o nome da sua pasta interna de configurações
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_cliente.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Tem certeza que ele está instalado e "
            "disponível na sua variável de ambiente PYTHONPATH? Você se esqueceu de "
            "ativar o ambiente virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
# cliente/utils.py

def validate_cpf_format(cpf_number):
    """
    Verifica se o CPF tem o formato correto (11 dígitos numéricos) 
    e retorna True se for válido.
    """
    # Remove caracteres de formatação
    cpf_clean = str(cpf_number).replace('.', '').replace('-', '')
    
    # 1. Checa se tem 11 dígitos
    if len(cpf_clean) != 11:
        return False

    # 2. Checa se é numérico
    if not cpf_clean.isdigit():
        return False
        
    return True
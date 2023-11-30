def validacion_usuario(cadena):
    caracteres_no_admitidos = False
    for char in cadena:
        if not (char.isalnum() or char in ['_', '-', '.']):
            caracteres_no_admitidos = True
    return 5 <= len(cadena) <= 15 and not caracteres_no_admitidos
    
def validacion_password(cadena):
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    caracteres_especiales = False
    caracteres_repetidos = False
    caracteres_necesarios = False

    for char in cadena:
        if char.isupper():
            tiene_mayuscula = True
        elif char.islower():
            tiene_minuscula = True
        elif char.isdigit():
            tiene_numero = True
        elif char in ['_', '-', '#', '*']:
            caracteres_especiales = True

    if tiene_mayuscula and tiene_minuscula and tiene_numero and caracteres_especiales:
        caracteres_necesarios = True

    for i in range(len(cadena) - 1):
        if cadena[i] == cadena[i + 1]:
            caracteres_repetidos = True

    return 4 <= len(cadena) <= 8 and caracteres_necesarios and not caracteres_repetidos
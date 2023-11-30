def cifrado_cesar(cadena, clave, cifrado):
    
    if cifrado == False:
        clave = int(clave) * -1
    i = 0
    cadena_nueva = ""
    while i < len(cadena):
        if cadena[i].isalpha():
            cadena_nueva += chr(ord(cadena[i]) + int(clave))
        elif cadena[i].isdigit():
            cadena_nueva += str(int(cadena[i]) + int(clave))
        else:
            cadena_nueva += cadena[i]
        i += 1
    return cadena_nueva
    
    if destinatario_validado:
        remitente = "usuario_actual"
        clave_actual = int(clave_entry.get())
        cifrado = tipo_cifrado[0] + str(clave_actual) if tipo_cifrado == "Cesar" else "A"
        mensaje_cifrado = cadena_nueva
    guardar_mensaje(destinatario_validado, remitente, cifrado, mensaje_cifrado)
        tipo_cifrado = "Cesar"
    else:
        result_string.set("Destinatario Inexistente")

def cifrado_atbash(cadena):
    cadena_nueva = ""
    for char in cadena:
        if char.isalpha():
            if char.isupper():
                cadena_nueva += chr(122 - (ord(char) - 65))
            else:
                cadena_nueva += chr(90 - (ord(char) - 97))
        elif char.isdigit():
           cadena_nueva += str(10 - int(char))
        else:
            cadena_nueva += char
    return cadena_nueva

    if destinatario_validado:
        remitente = "usuario_actual"
        clave_actual = int(clave_entry.get())
        cifrado = tipo_cifrado[0] + str(clave_actual) if tipo_cifrado == "Cesar" else "A"
            mensaje_cifrado = cadena_nueva
    guardar_mensaje(destinatario_validado, remitente, cifrado, mensaje_cifrado)
        tipo_cifrado = "Atbash"
    else:
        result_string.set("Destinatario Inexistente")


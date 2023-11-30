def cifrado_cesar(cadena, clave, cifrado):
    global destinatario_validado
    global tipo_cifrado
    
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
    
    if validar_destinatario(destinatario_validado):
        remitente = "usuario_actual"
        clave = int(clave_entry.get())
        cifrado = tipo_cifrado[0] + str(clave) if tipo_cifrado == "Cesar" else "A"
        mensaje_cifrado = cadena_nueva
        
        if validar_destinatario(destinatario_validado):
            with open('mensajes.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([destinatario_validado, remitente, cifrado, mensaje_cifrado])
                result_string.set("Mensaje Enviado")
        else:
            result_string.set("Destinatario Inexistente")
    
    if destinatario_validado: 
        cadena_nueva = mensaje_cifrado
        guardar_mensaje(destinatario_validado, mensaje_cifrado)
        tipo_cifrado = "Cesar"

def cifrado_atbash(cadena):
    global destinatario_validado
    global tipo_cifrado
    
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

    if validar_destinatario(destinatario_validado):
        remitente = "usuario_actual"
        clave = int(clave_entry.get())
        cifrado = tipo_cifrado[0] + str(clave) if tipo_cifrado == "Cesar" else "A"
        mensaje_cifrado = cadena_nueva
        
        if validar_destinatario(destinatario_validado):
            with open('mensajes.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([destinatario_validado, remitente, cifrado, mensaje_cifrado])
                result_string.set("Mensaje Enviado")
        else:
            result_string.set("Destinatario Inexistente")
    else:
        result_string.set("Destinatario Inexistente")
        
    if destinatario_validado: 
        mensaje_cifrado = cadenita
        guardar_mensaje(destinatario_validado, mensaje_cifrado)
        tipo_cifrado = "Atbash"

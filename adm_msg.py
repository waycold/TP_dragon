import csv

## NUEVAS FUNCIONES OBJETIVO 2 ##

def validar_destinatario(destinatario):
    destinatario_valido = False
    with open('resources/data.csv', 'r') as data:
        reader = csv.reader(data)
        for row in reader:
            if row[0] == destinatario or destinatario == '*':
                destinatario_valido = True
    return destinatario_valido

def guardar_mensaje(destinatario, mensaje_cifrado, tipo_cifrado, clave_entry, result_string):
    remitente = "usuario_actual"
    clave = int(clave_entry.get())

    if validar_destinatario(destinatario):
        cifrado = tipo_cifrado[0] + str(clave) if tipo_cifrado == "Cesar" else "A"

        with open('mensajes.csv', 'a',) as MENSAJES_ENVIADOS:
            writer = csv.writer(MENSAJES_ENVIADOS)
            writer.writerow([destinatario, remitente, cifrado, mensaje_cifrado])
            result_string.set("Mensaje Enviado")
    else:
        result_string.set("Destinatario Inexistente")

def aceptar_destinatario(windows, destinatario_entry):
    global destinatario_validado
    destinatario = destinatario_entry.get()
    if validar_destinatario(destinatario):
        print("Destinatario válido:", destinatario)
        destinatario_validado = destinatario
        windows.destroy()
        # ventana_atbash.destroy()
        
    else:
        print("Destinatario invalido")

def enviar_cesar(destinatario_validado, cadena_nueva, tipo_cifrado, clave_actual, result_string):
    """Facundo Rizzato
    Guarda el mensaje cifrado en el archivo mensajes.csv.
    """
    if destinatario_validado:
        remitente = "usuario_actual"
        # clave_actual = int(clave_entry.get())
        cifrado = tipo_cifrado[0] + str(clave_actual) if tipo_cifrado == "Cesar" else "A"
        mensaje_cifrado = cadena_nueva
        guardar_mensaje(destinatario_validado, remitente, cifrado, mensaje_cifrado)
        tipo_cifrado = "Cesar"
    else:
        result_string.set("Destinatario Inexistente")

def enviar_atbash(destinatario_validado, cadena_nueva, tipo_cifrado, clave_actual, result_string):
    """Facundo Rizzato
    Guarda el mensaje cifrado en el archivo mensajes.csv."""
    if destinatario_validado:
        remitente = "usuario_actual"
        # clave_actual = int(clave_entry.get())
        cifrado = tipo_cifrado[0] + str(clave_actual) if tipo_cifrado == "Cesar" else "A"
        mensaje_cifrado = cadena_nueva
        guardar_mensaje(destinatario_validado, remitente, cifrado, mensaje_cifrado)
        tipo_cifrado = "Atbash"
    else:
        result_string.set("Destinatario Inexistente")


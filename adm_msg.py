import csv
import cifrados

## NUEVAS FUNCIONES OBJETIVO 2 ##

def validar_destinatario(destinatario):
    destinatario_valido = False
    with open('resources/data.csv', 'r') as data:
        reader = csv.reader(data)
        for row in reader:
            if row[0] == destinatario or destinatario == '*':
                destinatario_valido = True
    return destinatario_valido

def guardar_mensaje(destinatario, mensaje_cifrado, tipo_cifrado, clave, error_msg):
    with open('resources/actual_user.csv', 'r') as actual_user:
        reader = csv.reader(actual_user)
        for row in reader:
            actual_user = row[0]
    if validar_destinatario(destinatario):
        cifrado = tipo_cifrado[0] + str(clave) if tipo_cifrado == "Cesar" else "A"
        with open('resources/mensajes.csv', 'a',) as MENSAJES_ENVIADOS:
            writer = csv.writer(MENSAJES_ENVIADOS)
            writer.writerow([destinatario, actual_user, cifrado, mensaje_cifrado])
            error_msg.config(text ="Mensaje Enviado")
    else:
        error_msg.config(text ="Destinatario Inexistente")

def aceptar_destinatario(destinatario, error_msg):
    if validar_destinatario(destinatario):
        error_msg.config(text = "destinatario valido", foreground="green")
    else:
        error_msg.config(text = "Destinatario Inexistente")

def enviar_cesar(destinatario, cadena, tipo_cifrado, clave_actual, error_msg):
    """Facundo Rizzato
    Guarda el mensaje cifrado en el archivo mensajes.csv.
    """
    if validar_destinatario(destinatario):
        tipo_cifrado = "Cesar"
        mensaje_cifrado = cifrados.cifrado_cesar(cadena, clave_actual, True)
        guardar_mensaje(destinatario, mensaje_cifrado, tipo_cifrado, clave_actual, error_msg)
    else:
        error_msg.config(text = "Error", foreground="red")

def enviar_atbash(destinatario, cadena, tipo_cifrado, clave_actual, error_msg):
    """Facundo Rizzato
    Guarda el mensaje cifrado en el archivo mensajes.csv."""
    if validar_destinatario(destinatario):
        tipo_cifrado = "Atbash"
        mensaje_cifrado = cifrados.cifrado_atbash(cadena) 
        guardar_mensaje(destinatario, mensaje_cifrado, tipo_cifrado, 0, error_msg)
    else:
        error_msg.set("Error", foreground="red")


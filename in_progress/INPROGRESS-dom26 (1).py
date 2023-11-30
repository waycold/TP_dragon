import tkinter as tk
from tkinter import ttk
import csv

tipo_cifrado = None

def only_numbers(P):
    return P.isdigit() or P == ""

def cifrado_cesar():
    global destinatario_validado
    global tipo_cifrado

    cadena = text_entry.get()
    clave = int(clave_entry.get())
    i = 0
    cadena_nueva = ""
    while i < len(cadena):
        if cadena[i].isalpha():
            if cadena[i].islower():
                cadena_nueva += chr(((ord(cadena[i]) - ord('a') + clave) % 26) + ord('a'))
            else:  
                cadena_nueva += chr(((ord(cadena[i]) - ord('A') + clave) % 26) + ord('A'))
        elif cadena[i].isdigit():
            cadena_nueva += str((int(cadena[i]) + clave) % 10)  
        else:
            cadena_nueva += cadena[i]
        i += 1
    result_string.set(cadena_nueva)
    
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

def cifrado_atbash():
    global destinatario_validado
    global tipo_cifrado
    
    cadena = text_entry.get()
    cadenita = ""
    abecedario = {
        "a": ["z", "Z"], "b": ["y", "Y"], "c": ["x", "X"], "d": ["w", "W"],
        "e": ["v", "V"], "f": ["u", "U"], "g": ["t", "T"], "h": ["s", "S"],
        "i": ["r", "R"], "j": ["q", "Q"], "k": ["p", "P"], "l": ["o", "O"],
        "m": ["ñ", "Ñ"], "n": ["n", "N"], "ñ": ["m", "M"], "o": ["l", "L"],
        "p": ["k", "K"], "q": ["j", "J"], "r": ["i", "I"], "s": ["h", "H"],
        "t": ["g", "G"], "u": ["f", "F"], "v": ["e", "E"], "w": ["d", "D"],
        "x": ["c", "C"], "y": ["b", "B"], "z": ["a", "A"]
    }
    numeros = {"1": "9", "2": "8", "3": "7", "4": "6", "5": "5", "6": "4", "7": "3", "8": "2", "9": "1"}

    minuscula = 0
    mayuscula = 1
    for caracter in cadena:
        if caracter.isalpha():
            if caracter.isupper():
                cadenita += abecedario[caracter.lower()][minuscula]
            else:
                cadenita += abecedario[caracter][mayuscula]
        elif caracter.isdigit():
            cadenita += numeros[caracter]
        else:
            cadenita += caracter

    result_string.set(cadenita)
    tipo_cifrado = "Atbash"
    
    if validar_destinatario(destinatario_validado):
        remitente = "usuario_actual"
        clave = int(clave_entry.get())
        cifrado = tipo_cifrado[0] + str(clave) if tipo_cifrado == "Cesar" else "A"
        mensaje_cifrado = cadenita
        
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
    
def descifrado_cesar():
    cadena = text_entry.get()
    clave = int(clave_entry.get())
    cadena_nueva = ""
    for letra in cadena:
        if letra.isalpha():
            cadena_nueva += chr(ord(letra) - clave)
        elif letra.isdigit():
            cadena_nueva += str(int(letra) - clave)
        else:
            cadena_nueva += letra
    result_string.set(cadena_nueva)
    
## NUEVAS FUNCIONES OBJETIVO 2 ##

def validar_destinatario(destinatario):
    destinatarios_validos = ['Nahuel', 'Facundo', 'Genesis', 'Valentin']
    if destinatario == '*':
        return True
    elif destinatario in destinatarios_validos:
        return True
    else:
        return False

def abrir_ventana_cesar():
    ventana_cesar = tk.Toplevel(root)
    ventana_cesar.title("Enviar mensaje cifrado con César")
    destinatario_entry = ttk.Entry(ventana_cesar, width=30, font=("Arial", 14))
    
    def aceptar_destinatario():
        global destinatario_validado
        destinatario = destinatario_entry.get()
        if validar_destinatario(destinatario):
            print("Destinatario válido:", destinatario)
            destinatario_validado = destinatario
            ventana_cesar.destroy()
            encryption_menu.pack()
        else:
            print("Destinatario invalido")
            
    destinatario_entry.pack()
    ttk.Button(ventana_cesar, text="Elegir Destinatario", command=aceptar_destinatario).pack()

def abrir_ventana_atbash():
    ventana_atbash = tk.Toplevel(root)
    ventana_atbash.title("Enviar mensaje cifrado con Atbash")
    destinatario_entry = ttk.Entry(ventana_atbash, width=30, font=("Arial", 14))
    
    def aceptar_destinatario():
        global destinatario_validado
        destinatario = destinatario_entry.get()
        if validar_destinatario(destinatario):
            print("Destinatario válido:", destinatario)
            destinatario_validado = destinatario
            ventana_atbash.destroy()
        else:
            print("Destinatario invalido")
            
    destinatario_entry.pack()        
    ttk.Button(ventana_atbash, text="Elegir Destinatario", command=aceptar_destinatario).pack()

def guardar_mensaje(destinatario, mensaje_cifrado):
    remitente = "usuario_actual"
    clave = int(clave_entry.get())

    if validar_destinatario(destinatario):
        cifrado = tipo_cifrado[0] + str(clave) if tipo_cifrado == "Cesar" else "A"

        with open('mensajes.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([destinatario, remitente, cifrado, mensaje_cifrado])
            result_string.set("Mensaje Enviado")
    else:
        result_string.set("Destinatario Inexistente")
    

def continue_pressed():
    main_menu.destroy()
    encryption_menu.pack()
    continue_text.grid(row=0, column=0, columnspan=100, pady=(0, 10))
    entered_text_description.grid(row=1, column=0, columnspan=100, pady=(0, 10))
    text_entry.grid(row=2, column=0, columnspan=2, pady=(0, 10))
    clave_entry_description.grid(row=3, column=0, columnspan=2, pady=(0, 10))
    clave_entry.grid(row=4, column=0, columnspan=2, pady=(0, 100))
    botton_cifrar_cesar.grid(row=5, column=0, pady=0, padx=0)
    botton_cifrar_atbash.grid(row=5, column=1, pady=0, padx=0)
    botton_descifrar_cesar.grid(row=6, column=0, pady=20, padx=40)
    botton_descifrar_atbash.grid(row=6, column=1, pady=20, padx=40)
    botton_enviar_mensaje_cesar.grid(row=7, column=0, pady=20, padx=40)
    botton_enviar_mensaje_atbash.grid(row=7, column=1, pady=20, padx=40)
    result_label.grid(row=7, column=0, columnspan=2, pady=20)

    
root = tk.Tk()

# Definir el main_menu
main_menu = tk.Frame(root, bg="#F5F5F5")

welcome_text = ttk.Label(main_menu, text="Bienvenido a la aplicación de mensajes secretos del grupo Dragon")
instructions_text = ttk.Label(main_menu, text="Para continuar, presione el botón 'Continuar' o cierre la ventana.", style='secondary.TLabel')
continue_button = ttk.Button(main_menu, text="Continuar", command=continue_pressed)
about_text = ttk.Label(main_menu, text="Construida por ...", font=("Arial", 10))

# Definir el encryption_menu y sus elementos
encryption_menu = tk.Frame(root, bd=5, padx=10, pady=10, bg="#F5F5F5")
entered_text_description = ttk.Label(encryption_menu, text="Ingrese el texto a cifrar/descifrar:", style='secondary.TLabel')
text_entry = ttk.Entry(encryption_menu, width=30, font=("Arial", 14), justify="left")
clave_entry_description = ttk.Label(encryption_menu, text="Ingrese la clave:", style='secondary.TLabel')
clave_entry = ttk.Entry(encryption_menu, width=10, font=("Arial", 14), justify="center")  # Aquí falta la configuración de textvariable y validaciones
continue_text = ttk.Label(encryption_menu, text="¡Has presionado Continuar!")
botton_cifrar_cesar = ttk.Button(encryption_menu, text="Cifrar con Cesar", command=cifrado_cesar)
botton_cifrar_atbash = ttk.Button(encryption_menu, text="Cifrar con Atbash", command=cifrado_atbash)
botton_descifrar_cesar = ttk.Button(encryption_menu, text="Descifrar con Cesar", command=descifrado_cesar)
botton_descifrar_atbash = ttk.Button(encryption_menu, text="Descifrar con Atbash", command=cifrado_atbash)
botton_enviar_mensaje_cesar = ttk.Button(encryption_menu, text="Enviar mensaje cifrado con Cesar", command=abrir_ventana_cesar)
botton_enviar_mensaje_atbash = ttk.Button(encryption_menu, text="Enviar mensaje cifrado con Atbash", command=abrir_ventana_atbash)
result_string = tk.StringVar()
result_label = ttk.Label(encryption_menu, text="", textvariable=result_string, font=("Arial", 14))


# Pack the widgets in main_menu
main_menu.pack()
welcome_text.pack(pady=20)
instructions_text.pack(pady=(300, 5))
continue_button.pack(pady=10)
about_text.pack(pady=20)

# Loop
root.mainloop()

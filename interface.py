import tkinter as tk
from tkinter import ttk


# functions

def only_numbers(P):
    return P.isdigit() or P == ""

def cifrado_cesar():
    cadena = text_entry.get()
    clave = int(clave_entry.get())
    i = 0
    cadena_nueva = ""
    while i < len(cadena):
        if cadena[i].isalpha():
            cadena_nueva += chr(ord(cadena[i]) + clave)
        elif cadena[i].isdigit():
            cadena_nueva += str(int(cadena[i]) + clave)
        else:
            cadena_nueva += cadena[i]
        i += 1
    result_string.set(cadena_nueva)


def cifrado_atbash():
    cadena = text_entry.get()
    i = 0
    cadenita = ""
    abecedario = {"a": ["z", "Z"], "b": ["y", "Y"], "c": ["x", "X"], "d": ["w", "W"],
                  "e": ["v", "V"], "f": ["u", "U"], "g": ["t", "T"], "h": ["s", "S"],
                  "i": ["r", "R"], "j": ["q", "Q"], "k": ["p", "P"], "l": ["o", "O"],
                  "m": ["ñ", "Ñ"], "n": ["n", "N"], "ñ": ["m", "M"], "o": ["l", "L"],
                  "p": ["k", "K"], "q": ["j", "J"], "r": ["i", "I"], "s": ["h", "H"],
                  "t": ["g", "G"], "u": ["f", "F"], "v": ["e", "E"], "w": ["d", "D"],
                  "x": ["c", "C"], "y": ["b", "B"], "z": ["a", "A"]}
    numeros = {"1": "9", "2": "8", "3": "7", "4": "6", "5": "5", "6": "4", "7": "3", "8": "2", "9": "1"}
    while i < len(cadena):
        if cadena[i].isalpha():
            if cadena[i].isupper():
                cadenita += abecedario[cadena[i].lower()][0]
            else:
                cadenita += abecedario[cadena[i]][1]
        elif cadena[i].isdigit():
            cadenita += numeros[cadena[i]]
        else:
            cadenita += cadena[i]
        i += 1
    result_string.set(cadenita)


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

def continue_pressed():
    main_menu.destroy()

    encryption_menu.pack()
    continue_text.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    entered_text_description.grid(row=1, column=0, columnspan=2, pady=(0, 10))
    text_entry.grid(row=2, column=0, columnspan=2, pady=(0, 10))
    clave_entry_description.grid(row=3, column=0, columnspan=2, pady=(0, 10))
    clave_entry.grid(row=4, column=0, columnspan=2, pady=(0, 100))
    botton_cifrar_cesar.grid(row=5, column=0, pady=20, padx=40)
    botton_cifrar_atbash.grid(row=5, column=1, pady=20, padx=40)
    botton_descifrar_cesar.grid(row=6, column=0, pady=20, padx=40)
    botton_descifrar_atbash.grid(row=6, column=1, pady=20, padx=40)
    result_label.grid(row=7, column=0, columnspan=2, pady=20)



#window
root = tk.Tk()

root.title("TP Grupal Parte 1 - Grupo: Dragon")
root.geometry("900x600")
root.iconbitmap('icon.ico')
root.configure(bg="#F5F5F5")


#validacion
var = tk.StringVar()
validacion = root.register(only_numbers)


#style
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=("Arial", 14), background="#4F709C", padding=10, pady=5, foreground="white", borderwidth=0, width=20)
style.configure('TLabel', background="#F5F5F5", font=("Arial", 18))

style.configure('secondary.TLabel', font=("Helvetica", 10), foreground="#253346")


style.map('TButton', background=[('active', '#47648B')])


#frames and widgets
main_menu = tk.Frame(root, bg="#F5F5F5")

welcome_text = ttk.Label(main_menu, text="Bienvenido a la aplicación de mensajes secretos del grupo Dragon")
instructions_text = ttk.Label(main_menu, text="Para continuar, presione el botón 'Continuar' o cierre la ventana.", style='secondary.TLabel')
continue_button = ttk.Button(main_menu, text="Continuar", command=continue_pressed)
about_text = ttk.Label(main_menu, text="Construida por ...", font=("Arial", 10))


encryption_menu = tk.Frame(root, bd=5, padx=10, pady=10, bg="#F5F5F5")

entered_text_description = ttk.Label(encryption_menu, text="Ingrese el texto a cifrar/descifrar:", style='secondary.TLabel')
text_entry = ttk.Entry(encryption_menu, width=30, font=("Arial", 14), justify="center")
clave_entry_description = ttk.Label(encryption_menu, text="Ingrese la clave:", style='secondary.TLabel')
#.....................
clave_entry = ttk.Entry(encryption_menu, width=10, font=("Arial", 14), justify="center",textvariable=var, validate="key", validatecommand=(validacion, "%P"))
#.....................
continue_text = ttk.Label(encryption_menu, text="¡Has presionado Continuar!")
botton_cifrar_cesar = ttk.Button(encryption_menu, text="Cifrar con Cesar", command=cifrado_cesar)
botton_cifrar_atbash = ttk.Button(encryption_menu, text="Cifrar con Atbash", command=cifrado_atbash)
botton_descifrar_cesar = ttk.Button(encryption_menu, text="Descifrar con Cesar", command=descifrado_cesar)
botton_descifrar_atbash = ttk.Button(encryption_menu, text="Descifrar con Atbash", command=cifrado_atbash)
result_string = tk.StringVar()
result_label = ttk.Label(encryption_menu, text="", textvariable=result_string, font=("Arial", 14))


# Pack the widgets main menu
main_menu.pack()
welcome_text.pack(pady=20)
instructions_text.pack(pady=(300, 5))
continue_button.pack(pady=10)
about_text.pack(pady=20)

#loop
root.mainloop()

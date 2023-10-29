import tkinter as tk

# Función para continuar
def cifrado_cesar():
    cadena = entry.get()
    clave = 3
    lista=[]
    i=0
    cadena_nueva="" 
    while i<len(cadena):
        if cadena[i].isalpha():
            cadena_nueva+= chr(ord(cadena[i])+clave)
        elif cadena[i].isdigit():
            cadena_nueva+= str(int(cadena[i])+clave)
        else:
            cadena_nueva+=cadena[i]
        i+=1
    resultado_string.set(cadena_nueva)

def continue_pressed():
    main_menu.destroy()
    

    cifrado_menu.pack()
    new_label.grid(row=0, column=1, padx=10, pady=10)
    entry.grid(row=1, column=1, padx=10, pady=20)
    botton_cifrar_cesar.grid(row=2, column=0, padx=10, pady=(100, 10))
    botton_cifrar_atbash.grid(row=2, column=2, padx=10, pady=(100, 10))
    botton_descifrar_cesar.grid(row=3, column=0, padx=10, pady=10)
    botton_descifrar_atbash.grid(row=3, column=2, padx=10, pady=10)
    resultado_label.grid(row=4, column=1, padx=10, pady=10)



root = tk.Tk()

root.title("TP Grupal Parte 1 - Grupo: Dragon")
root.geometry("900x600")
root.iconbitmap('icon.ico')
root.configure(bg="#F5F5F5")


main_menu = tk.Frame(root, bg="#F5F5F5")

welcome_text = tk.Label(main_menu, text="Bienvenido a la aplicación de mensajes secretos del grupo Dragon", font=("Arial", 20), bg="#F5F5F5")
instructions_text = tk.Label(main_menu, text="Para continuar, presione el botón 'Continuar' o cierre la ventana.", font=("Arial", 12), bg="#F5F5F5")
continue_button = tk.Button(main_menu, text="Continuar", command=continue_pressed, font=("Arial", 14), bg="#4F709C", fg="white", padx=10, pady=5)
about_text = tk.Label(main_menu, text="Construida por ...", font=("Arial", 10))

cifrado_menu = tk.Frame(root, bd=5, padx=10, pady=10)

entry = tk.Entry(cifrado_menu, width=30, font=("Arial", 14), justify="center")
new_label = tk.Label(cifrado_menu, text="¡Has presionado Continuar!", font=("Arial", 16))
botton_cifrar_cesar = tk.Button(cifrado_menu, text="Cifrar con Cesar", command=cifrado_cesar, font=("Arial", 14), bg="#4F709C", fg="white", padx=10, pady=5)
botton_cifrar_atbash = tk.Button(cifrado_menu, text="Cifrar con Atbash", font=("Arial", 14), bg="#4F709C", fg="white", padx=10, pady=5)
botton_descifrar_cesar = tk.Button(cifrado_menu, text="Descifrar con Cesar", font=("Arial", 14), bg="#4F709C", fg="white", padx=10, pady=5)
botton_descifrar_atbash = tk.Button(cifrado_menu, text="Descifrar con Atbash", font=("Arial", 14), bg="#4F709C", fg="white", padx=10, pady=5)
resultado_string = tk.StringVar()
resultado_label = tk.Label(cifrado_menu, text="a", textvariable=resultado_string, font=("Arial", 14), bg="#F5F5F5")

# Pack the widgets into the window
main_menu.pack()
welcome_text.pack(pady=20)
instructions_text.pack()
continue_button.pack(pady=10)
about_text.pack(pady=20)


root.mainloop()

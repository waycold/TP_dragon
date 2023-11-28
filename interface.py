import tkinter as tk
from tkinter import ttk, PhotoImage
import cifrados


# functions
def actualizar_label(tipo_cifrado):
    if tipo_cifrado == "Cesar":
        texto_cifrado = cifrados.cifrado_cesar(texto_original.get(), clave_entry.get(), True)
    elif tipo_cifrado == "des_Cesar":
        texto_cifrado = cifrados.cifrado_cesar(texto_original.get(), clave_entry.get(), False)
    elif tipo_cifrado == "Atbash":
        texto_cifrado = cifrados.cifrado_atbash(texto_original.get())
    else:
        texto_cifrado = "Tipo de cifrado no válido"

    result_label.config(text=texto_cifrado)

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
root.iconbitmap('resourses\icon.ico')
root.configure(bg="#F5F5F5")


#validacion
var = tk.StringVar()
validacion = root.register(lambda P: P.isdigit() or P == "")

user_image = PhotoImage(file = "user_icon.png")


#style
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=("Arial", 14), background="#4F709C", padding=10, pady=5, foreground="white", borderwidth=0, width=20)
style.configure('image.TButton', image=user_image, padding=10, borderwidth=0, width=20, background="F5F5F5")
style.configure('TLabel', background="#F5F5F5", font=("Arial", 18))

style.configure('secondary.TLabel', font=("Helvetica", 10), foreground="#253346")

style.map('TButton', background=[('active', '#47648B')])


#frames and widgets
main_menu = tk.Frame(root, bg="#F5F5F5")

user_button = ttk.Button(root, style="image.TButton")
welcome_text = ttk.Label(main_menu, text="Bienvenido a la aplicación de mensajes secretos del grupo Dragon")
instructions_text = ttk.Label(main_menu, text="Para continuar, presione el botón 'Continuar' o cierre la ventana.", style='secondary.TLabel')
continue_button = ttk.Button(main_menu, text="Continuar", command=continue_pressed)
about_text = ttk.Label(main_menu, text="Construida por Facundo Rizzato, ...", font=("Arial", 10))

encryption_menu = tk.Frame(root, bd=5, padx=10, pady=10, bg="#F5F5F5")

entered_text_description = ttk.Label(encryption_menu, text="Ingrese el texto a cifrar/descifrar:", style='secondary.TLabel')
texto_original = tk.StringVar()
text_entry = ttk.Entry(encryption_menu, width=30, font=("Arial", 14), justify="center", textvariable=texto_original)
clave_entry_description = ttk.Label(encryption_menu, text="Ingrese la clave:", style='secondary.TLabel')
clave_entry = ttk.Entry(encryption_menu, width=10, font=("Arial", 14), justify="center",textvariable=var, validate="key", validatecommand=(validacion, "%P"))
continue_text = ttk.Label(encryption_menu, text="¡Has presionado Continuar!")

botton_cifrar_cesar = ttk.Button(encryption_menu, text="Cifrar con Cesar", command=lambda: actualizar_label("Cesar"))
botton_cifrar_atbash = ttk.Button(encryption_menu, text="Cifrar con Atbash", command=lambda: actualizar_label("Atbash"))
botton_descifrar_cesar = ttk.Button(encryption_menu, text="Descifrar con Cesar", command=lambda: actualizar_label("des_Cesar"))
botton_descifrar_atbash = ttk.Button(encryption_menu, text="Descifrar con Atbash", command=lambda: actualizar_label("Atbash"))

result_string = tk.StringVar()
result_label = ttk.Label(encryption_menu, text="", font=("Arial", 14))



# Packing
user_button.pack()
main_menu.pack()
welcome_text.pack(pady=20)
instructions_text.pack(pady=(300, 5))
continue_button.pack(pady=10)
about_text.pack(pady=20)

#loop
root.mainloop()

import tkinter as tk
from tkinter import ttk
import cifrados, admin_users, adm_msg
import csv

options = []
with open('resources\preguntas.csv', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        options.append(fila[1])

# functions
def actualizar_label(tipo_cifrado):
    """Facundo Rizzato
    Actualiza el label con el texto cifrado o descifrado, dependiendo del tipo de cifrado seleccionado.
    """
    if tipo_cifrado == "Cesar":
        texto_cifrado = cifrados.cifrado_cesar(texto_original.get(), clave_entry.get(), True)
    elif tipo_cifrado == "des_Cesar":
        texto_cifrado = cifrados.cifrado_cesar(texto_original.get(), clave_entry.get(), False)
    elif tipo_cifrado == "Atbash":
        texto_cifrado = cifrados.cifrado_atbash(texto_original.get())
    else:
        texto_cifrado = "Tipo de cifrado no válido"

    result_label.config(text=texto_cifrado)


# windows
def encryption_windows():
    """Facundo Rizzato
    Abre la ventana de cifrado.
    """
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
    botton_enviar_mensaje_cesar.grid(row=7, column=0, pady=20, padx=40)
    botton_enviar_mensaje_atbash.grid(row=7, column=1, pady=20, padx=40)
    result_label.grid(row=7, column=0, columnspan=2, pady=20)

def sign_up_windows():
    """Facundo Rizzato
    Abre la ventana de registro.
    """
    sign_up = tk.Toplevel(root)
    sign_up.title("Registrarse")
    sign_up.geometry("500x500")
    sign_up.iconbitmap('resources\icon.ico')

    user_title = ttk.Label(sign_up, text="Usuario:", style='secondary.TLabel')
    user_entry = ttk.Entry(sign_up, width=50)
    password_title = ttk.Label(sign_up, text="Contraseña:", style='secondary.TLabel')
    password_entry = ttk.Entry(sign_up, width=50)
    recuperacion_title = ttk.Label(sign_up, text="Pregunta de recuperación:", style='secondary.TLabel')
    recuperacion_options = ttk.Combobox(sign_up, width=50, values=options, state="readonly")
    recuperacion = ttk.Entry(sign_up, width=50)
    error_msg = ttk.Label(sign_up, text="", foreground="red", style='secondary.TLabel')
    save_button = ttk.Button(sign_up, text="Guardar", command=lambda: admin_users.registro(user_entry.get(), password_entry.get(), error_msg, user_entry, password_entry, recuperacion.get(), recuperacion_options.get()))

    user_title.pack(pady=5)
    user_entry.pack(pady=10)
    password_title.pack(pady=5)
    password_entry.pack(pady=10)
    recuperacion_title.pack(pady=5)
    recuperacion_options.pack(pady=10)
    recuperacion.pack(pady=20)
    error_msg.pack(pady=5)
    save_button.pack(pady=10)

def login_windows():
    """Facundo Rizzato
    Abre la ventana de inicio de sesión.
    """
    login_frame = tk.Toplevel(root)
    login_frame.title("Iniciar sesión")
    login_frame.geometry("500x500")
    login_frame.iconbitmap('resources\icon.ico')

    user_title = ttk.Label(login_frame, text="Usuario:", style='secondary.TLabel')
    user_entry = ttk.Entry(login_frame, width=50)
    password_title = ttk.Label(login_frame, text="Contraseña:", style='secondary.TLabel')
    password_entry = ttk.Entry(login_frame, width=50)
    error_msg = ttk.Label(login_frame, text="", foreground="red", style='secondary.TLabel')
    recuperacion_button = ttk.Button(login_frame, text="Recuperar contraseña", command=recuperacion_windows)
    login_button = ttk.Button(login_frame, text="Iniciar sesión", command=lambda: admin_users.login(user_entry.get(), password_entry.get(), error_msg, login_frame, encryption_windows))

    user_title.pack(pady=5)
    user_entry.pack(pady=10)
    password_title.pack(pady=5)
    password_entry.pack(pady=10)
    recuperacion_button.pack(pady=10)
    error_msg.pack(pady=5)
    login_button.pack(pady=10)

def recuperacion_windows():
    """Facundo Rizzato
    Abre la ventana de recuperación de contraseña.
    """
    recuperacion_windows = tk.Toplevel(root)

    recuperacion_windows.title("Recuperación de contraseña")
    recuperacion_windows.geometry("500x500")
    recuperacion_windows.iconbitmap('resources\icon.ico')

    insert_user_frame = tk.Frame(recuperacion_windows, bg="#F5F5F5")
    insert_recuperacion_frame = tk.Frame(recuperacion_windows, bg="#F5F5F5")

    user_title = ttk.Label(insert_user_frame, text="Usuario:", style='secondary.TLabel')
    user_entry = ttk.Entry(insert_user_frame, width=50)
    error_msg = ttk.Label(insert_user_frame, text="", foreground="red", style='secondary.TLabel')
    validar_button = ttk.Button(insert_user_frame, text="Verificar", command=lambda: admin_users.recuperacion_button_pressed(user_entry.get(), error_msg, insert_user_frame, insert_recuperacion_frame, recuperacion_windows))

    insert_user_frame.pack()
    user_title.pack(pady=5)
    user_entry.pack(pady=10)
    error_msg.pack(pady=5)
    validar_button.pack(pady=10)

# objetivo2
def windows_send_cesar():
    ventana_cesar = tk.Toplevel(root)
    ventana_cesar.title("Enviar mensaje cifrado con César")
    destinatario_entry = ttk.Entry(ventana_cesar, width=30, font=("Arial", 14))
    destinatario_entry.pack()
    destinatario_button = ttk.Button(ventana_cesar, text="Elegir Destinatario", command=adm_msg.aceptar_destinatario)
    send_button = ttk.Button(ventana_cesar, text="Enviar")
    destinatario_button.pack(pady=10)
    send_button.pack(pady=10)

def windows_send_atbash():
    ventana_atbash = tk.Toplevel(root)
    ventana_atbash.title("Enviar mensaje cifrado con Atbash")
    destinatario_entry = ttk.Entry(ventana_atbash, width=30, font=("Arial", 14))           
    destinatario_entry.pack()       
    destinatario_button = ttk.Button(ventana_atbash, text="Elegir Destinatario", command=adm_msg.aceptar_destinatario)
    send_button = ttk.Button(ventana_atbash, text="Enviar")
    destinatario_button.pack(pady=10)
    send_button.pack(pady=10)

root = tk.Tk()

root.title("TP Grupal Parte 1 - Grupo: Dragon")
root.geometry("900x600")
root.iconbitmap('resources\icon.ico')
root.configure(bg="#F5F5F5")

#validacion
var = tk.StringVar()
validacion = root.register(lambda P: P.isdigit() or P == "")


#style
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=("Arial", 14), background="#4F709C", padding=10, pady=5, foreground="white", borderwidth=0, width=20)
style.configure('TLabel', background="#F5F5F5", font=("Arial", 18))
style.configure('TEntry', background="#F5F5F5", font=("Arial", 14), borderwidth=0, width=30)

style.configure('secondary.TLabel', font=("Helvetica", 10), foreground="#253346")

style.map('TButton', background=[('active', '#47648B')])

# main menu
main_menu = tk.Frame(root, bg="#F5F5F5")

welcome_text = ttk.Label(main_menu, text="Bienvenido a la aplicación de mensajes secretos del grupo Dragon")
instructions_text = ttk.Label(main_menu, text="Para continuar, presione el botón 'Continuar' o cierre la ventana.", style='secondary.TLabel')
signup_button = ttk.Button(main_menu, text="Registrarse", command=sign_up_windows)
login_button = ttk.Button(main_menu, text="Iniciar sesión", command=login_windows)
about_text = ttk.Label(main_menu, text="Construida por Facundo Rizzato, ...", font=("Arial", 10))

# encryption menu
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

botton_enviar_mensaje_cesar = ttk.Button(encryption_menu, text="Enviar mensaje cifrado con Cesar", command=windows_send_cesar)
botton_enviar_mensaje_atbash = ttk.Button(encryption_menu, text="Enviar mensaje cifrado con Atbash", command=windows_send_atbash)

result_string = tk.StringVar()
result_label = ttk.Label(encryption_menu, text="", font=("Arial", 14))



# Packing
main_menu.pack()
welcome_text.pack(pady=20)
instructions_text.pack(pady=(250, 5))
login_button.pack(pady=10)
signup_button.pack(pady=10)
about_text.pack(pady=20)

#loop
root.mainloop()
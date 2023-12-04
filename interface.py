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
    mensajes.grid(row=4, column=0, columnspan=2, pady=(0, 10))
    botton_cifrar_cesar.grid(row=5, column=0, pady=20, padx=40)
    botton_cifrar_atbash.grid(row=5, column=1, pady=20, padx=40)
    botton_descifrar_cesar.grid(row=6, column=0, pady=20, padx=40)
    botton_descifrar_atbash.grid(row=6, column=1, pady=20, padx=40)
    botton_enviar_mensaje_cesar.grid(row=7, column=0, pady=20, padx=40)
    botton_enviar_mensaje_atbash.grid(row=7, column=1, pady=20, padx=40)
    result_label.grid(row=8, column=0, columnspan=2, pady=(0, 10))

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
    ventana_cesar.geometry("500x500")
    destinatario_Label = ttk.Label(ventana_cesar, text="Destinatario:", font=("Arial", 14))
    destinatario_entry = ttk.Entry(ventana_cesar, width=30, font=("Arial", 14))
    destinatario_button = ttk.Button(ventana_cesar, text="Elegir Destinatario", command=lambda: adm_msg.aceptar_destinatario(destinatario_entry.get(), error_msg))
    msg_Label = ttk.Label(ventana_cesar, text="Mensaje:", font=("Arial", 14))
    msg = ttk.Entry(ventana_cesar, width=30, font=("Arial", 14))
    clave_Label = ttk.Label(ventana_cesar, text="Clave:", font=("Arial", 14))
    clave = ttk.Entry(ventana_cesar, width=30, font=("Arial", 14))
    error_msg = ttk.Label(ventana_cesar, text="", foreground="red", style='secondary.TLabel')
    send_button = ttk.Button(ventana_cesar, text="Enviar", command=lambda: adm_msg.enviar_cesar(destinatario_entry.get(), msg.get(), "Cesar", clave.get(), error_msg))
    destinatario_Label.pack()
    destinatario_entry.pack()
    msg_Label.pack(pady=10)
    msg.pack(pady=10)
    clave_Label.pack(pady=10)
    clave.pack(pady=10)
    destinatario_button.pack(pady=10)
    error_msg.pack(pady=5)
    send_button.pack(pady=10)

def windows_send_atbash():
    ventana_atbash = tk.Toplevel(root)
    ventana_atbash.title("Enviar mensaje cifrado con Atbash")
    ventana_atbash.geometry("500x500")
    destinatario_Label = ttk.Label(ventana_atbash, text="Destinatario:", font=("Arial", 14))
    destinatario_entry = ttk.Entry(ventana_atbash, width=30, font=("Arial", 14))           
    msg_Label = ttk.Label(ventana_atbash, text="Mensaje:", font=("Arial", 14))
    msg = ttk.Entry(ventana_atbash, width=30, font=("Arial", 14))
    destinatario_button = ttk.Button(ventana_atbash, text="Elegir Destinatario", command=lambda: adm_msg.aceptar_destinatario(destinatario_entry.get(), error_msg))
    error_msg = ttk.Label(ventana_atbash, text="", foreground="red", style='secondary.TLabel')
    send_button = ttk.Button(ventana_atbash, text="Enviar", command=lambda: adm_msg.enviar_atbash(destinatario_entry.get(), msg.get(), "Atbash", 0, error_msg))
    destinatario_Label.pack()
    destinatario_entry.pack()
    msg_Label.pack(pady=10)       
    msg.pack(pady=10)
    destinatario_button.pack(pady=10)
    error_msg.pack(pady=5)
    send_button.pack(pady=10)

#objetivo 3

def windows_mensajes():
    ventana_mensajes = tk.Toplevel(root)
    ventana_mensajes.title("Mensajes recibidos")
    ventana_mensajes.geometry("500x500")
    ventana_mensajes.iconbitmap('resources\icon.ico')
    ventana_mensajes.configure(bg="#E7E7E7")

    mensaje_label = ttk.Label(ventana_mensajes, text="Mensajes recibidos:", font=("Arial", 16), background="#E7E7E7")
    mensaje_label.pack(pady=10)

    with open('resources/actual_user.csv', 'r') as actual_user:
        reader = csv.reader(actual_user)
        fila = next(reader)
        actual_user = fila[0]

    with open('resources/mensajes.csv', 'r') as mensajes:
        reader = csv.reader(mensajes)
        for row in reader:
            mensaje = row[3]
            tipo_cifrado = row[2]
            if tipo_cifrado[0] == "C":
                clave = tipo_cifrado[1:]
                mensaje = cifrados.cifrado_cesar(mensaje, clave, False)
            else:
                mensaje = cifrados.cifrado_atbash(mensaje)
            
            if row[1] == actual_user:
                if row[0] == "*":
                    mensaje = "[All]: " + mensaje
                    mensaje_label = ttk.Label(ventana_mensajes, text=mensaje, font=("Arial", 12), foreground="#567BB4", background="#D9E1F2")
                    mensaje_label.pack(pady=2, side="top", anchor="w", fill="x", padx=10)
                else:
                    mensaje = row[0] + ": " + mensaje
                    mensaje_label = ttk.Label(ventana_mensajes, text=mensaje, font=("Arial", 12))
                    mensaje_label.pack(pady=2, side="top", anchor="w", fill="x", padx=10)
            else:
                if row[0] == "*":
                    mensaje = "[All]: " + mensaje
                    mensaje_label = ttk.Label(ventana_mensajes, text=mensaje, font=("Arial", 12), foreground="#567BB4")
                    mensaje_label.pack(pady=2, side="top", anchor="w", fill="x", padx=10)

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
# temporal_button = ttk.Button(main_menu, text="Continuar", command=encryption_windows)
about_text = ttk.Label(main_menu, text="Construida por Facundo Rizzato, ...", font=("Arial", 10))

# encryption menu
encryption_menu = tk.Frame(root, bd=5, padx=10, pady=10, bg="#F5F5F5")

entered_text_description = ttk.Label(encryption_menu, text="Ingrese el texto a cifrar/descifrar:", style='secondary.TLabel')
texto_original = tk.StringVar()
text_entry = ttk.Entry(encryption_menu, width=30, font=("Arial", 14), justify="center", textvariable=texto_original)
clave_entry_description = ttk.Label(encryption_menu, text="Ingrese la clave:", style='secondary.TLabel')
clave_entry = ttk.Entry(encryption_menu, width=10, font=("Arial", 14), justify="center",textvariable=var, validate="key", validatecommand=(validacion, "%P"))
continue_text = ttk.Label(encryption_menu, text="¡Has presionado Continuar!")
mensajes = ttk.Button(encryption_menu, text="Mensajes recibidos", command=windows_mensajes)

botton_cifrar_cesar = ttk.Button(encryption_menu, text="Cifrar con Cesar", command=lambda: actualizar_label("Cesar"))
botton_cifrar_atbash = ttk.Button(encryption_menu, text="Cifrar con Atbash", command=lambda: actualizar_label("Atbash"))
botton_descifrar_cesar = ttk.Button(encryption_menu, text="Descifrar con Cesar", command=lambda: actualizar_label("des_Cesar"))
botton_descifrar_atbash = ttk.Button(encryption_menu, text="Descifrar con Atbash", command=lambda: actualizar_label("Atbash"))

botton_enviar_mensaje_cesar = ttk.Button(encryption_menu, text="Enviar Cesar", command=windows_send_cesar)
botton_enviar_mensaje_atbash = ttk.Button(encryption_menu, text="Enviar Atbash", command=windows_send_atbash)

result_string = tk.StringVar()
result_label = ttk.Label(encryption_menu, text="", font=("Arial", 14))



# Packing
main_menu.pack()
welcome_text.pack(pady=20)
instructions_text.pack(pady=(250, 5))
# temporal_button.pack(pady=10)
login_button.pack(pady=10)
signup_button.pack(pady=10)
about_text.pack(pady=20)

#loop
root.mainloop()
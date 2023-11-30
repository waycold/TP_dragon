import tkinter as tk
from tkinter import ttk, PhotoImage
import cifrados, validation
import csv

options = []
with open('resourses\preguntas.csv', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        options.append(fila[1])

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

def sign_up_windows():
    sign_up = tk.Toplevel(root)
    sign_up.title("Registrarse")
    sign_up.geometry("500x500")
    sign_up.iconbitmap('resourses\icon.ico')

    user_title = ttk.Label(sign_up, text="Usuario:", style='secondary.TLabel')
    user_entry = ttk.Entry(sign_up, width=50)
    password_title = ttk.Label(sign_up, text="Contraseña:", style='secondary.TLabel')
    password_entry = ttk.Entry(sign_up, width=50)
    recuperacion_title = ttk.Label(sign_up, text="Pregunta de recuperación:", style='secondary.TLabel')
    recuperacion_options = ttk.Combobox(sign_up, width=50, values=options, state="readonly")
    recuperacion = ttk.Entry(sign_up, width=50)
    error_msg = ttk.Label(sign_up, text="", foreground="red", style='secondary.TLabel')
    save_button = ttk.Button(sign_up, text="Guardar", command=lambda: registro(user_entry.get(), password_entry.get(), error_msg, user_entry, password_entry, recuperacion.get(), recuperacion_options.get()))

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
    login_windows = tk.Toplevel(root)
    login_windows.title("Iniciar sesión")
    login_windows.geometry("500x500")
    login_windows.iconbitmap('resourses\icon.ico')

    user_title = ttk.Label(login_windows, text="Usuario:", style='secondary.TLabel')
    user_entry = ttk.Entry(login_windows, width=50)
    password_title = ttk.Label(login_windows, text="Contraseña:", style='secondary.TLabel')
    password_entry = ttk.Entry(login_windows, width=50)
    error_msg = ttk.Label(login_windows, text="", foreground="red", style='secondary.TLabel')
    recuperacion_button = ttk.Button(login_windows, text="Recuperar contraseña", command=recuperacion_windows)
    login_button = ttk.Button(login_windows, text="Iniciar sesión", command=lambda: login(user_entry.get(), password_entry.get(), error_msg, user_entry, password_entry))

    user_title.pack(pady=5)
    user_entry.pack(pady=10)
    password_title.pack(pady=5)
    password_entry.pack(pady=10)
    recuperacion_button.pack(pady=10)
    error_msg.pack(pady=5)
    login_button.pack(pady=10)

def recuperacion_windows():
    recuperacion_windows = tk.Toplevel(root)

    recuperacion_windows.title("Recuperación de contraseña")
    recuperacion_windows.geometry("500x500")
    recuperacion_windows.iconbitmap('resourses\icon.ico')

    insert_user_frame = tk.Frame(recuperacion_windows, bg="#F5F5F5")
    insert_recuperacion_frame = tk.Frame(recuperacion_windows, bg="#F5F5F5")

    user_title = ttk.Label(insert_user_frame, text="Usuario:", style='secondary.TLabel')
    user_entry = ttk.Entry(insert_user_frame, width=50)
    validar_button = ttk.Button(insert_user_frame, text="Verificar")


    # recuperacion_title = ttk.Label(recuperacion_windows, text="Pregunta de recuperación:", style='secondary.TLabel')
    # recuperacion_pregunta = ttk.Label(recuperacion_windows, text="", style='secondary.TLabel')
    # recuperacion_entry = ttk.Entry(recuperacion_windows, width=50)
    # error_msg = ttk.Label(recuperacion_windows, text="", foreground="red", style='secondary.TLabel')
    # save_button = ttk.Button(recuperacion_windows, text="Verificar", command=lambda: recuperacion(user_entry.get(), recuperacion_entry.get(), error_msg))

    insert_user_frame.pack()
    user_title.pack(pady=5)
    user_entry.pack(pady=10)
    validar_button.pack(pady=10)
    # recuperacion_title.pack(pady=5)
    # recuperacion_pregunta.pack(pady=10)
    # recuperacion_entry.pack(pady=20)
    # error_msg.pack(pady=5)
    # save_button.pack(pady=10)

# def recuperacion(user, recuperacion, pregunta, error_msg_label):
#     usuarios = []
#     with open('resourses/data.csv', newline='', encoding='utf-8') as archivo_csv:
#         lector_csv = csv.reader(archivo_csv)
#         for fila in lector_csv:
#             usuarios.append(fila)
#             id_pregunta = fila[2]

#     with open('resourses/preguntas.csv', newline='', encoding='utf-8') as archivo_csv:
#         lector_csv = csv.reader(archivo_csv)
#         for fila in lector_csv:
#             if fila[0] == id_pregunta:
#                 pregunta.config(text=fila[1])

#     encontrado = False
#     for i, fila in enumerate(usuarios):
#         if fila[0] == user:
#             encontrado = True
#             if fila[3] == recuperacion and int(fila[4]) == 3:
#                 error_msg_label.config(text=fila[1], foreground="#00f")
#                 usuarios[i] = [fila[0], fila[1], fila[2], fila[3], 0]
#             elif fila[3] == recuperacion and int(fila[4]) > 3:
#                 error_msg_label.config(text="Usuario bloqueado.")
#             else:
#                 intentos_restantes = 2 - int(fila[4])
#                 error_msg_label.config(text=f"Usuario o pregunta de recuperación incorrectos. Intentos restantes: {intentos_restantes}")
#                 fila[4] = str(int(fila[4]) + 1)

#     if not encontrado:
#         error_msg_label.config(text="Usuario no encontrado.")

#     with open('resourses/data.csv', 'w', newline='') as archivo_csv:
#         escritor_csv = csv.writer(archivo_csv)
#         escritor_csv.writerows(usuarios)

def validar_button_pressed(user, error_msg_label, frame):
    with open('resourses/data.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        
        usuario_encontrado = False
        for fila in lector_csv:
            if fila[0] == user:
                usuario_encontrado = True
                if int(fila[4]) <= 3:
                    frame.destroy()
                else:
                    error_msg_label.config(text="Usuario bloqueado.")
                
        if not usuario_encontrado:
            error_msg_label.config(text="Usuario o contraseña incorrectos.")

def login(user, password, error_msg_label, entry_user, entry_password):
    with open('resourses\data.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        
        usuario_encontrado = False
        for fila in lector_csv:
            if fila[0] == user and fila[1] == password:
                usuario_encontrado = True
                if int(fila[4]) <= 3:
                    error_msg_label.config(text="Usuario logueado correctamente.", foreground="#00f")
                    entry_user.delete(0, tk.END)
                    entry_password.delete(0, tk.END)
                    continue_pressed()
                else:
                    error_msg_label.config(text="Usuario bloqueado.")
                
        if not usuario_encontrado:
            error_msg_label.config(text="Usuario o contraseña incorrectos.")

def registro(user, password, error_msg_label, entry_user, entry_password, recuperacion, recuperacion_options):
    usuario_existente = False
    id_recuperacion = None
    
    with open('resourses/data.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if fila[0] == user:
                usuario_existente = True
                error_msg_label.config(text="Usuario ya existente.")
    
    with open('resourses/preguntas.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if fila[1] == recuperacion_options:
                id_recuperacion = fila[0]
    
    if not usuario_existente and id_recuperacion is not None:
        if validation.validacion_usuario(user) and validation.validacion_password(password):
            with open('resourses/data.csv', 'a', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerow([user, password, id_recuperacion, recuperacion, 0])
    
            error_msg_label.config(text="Usuario registrado correctamente.", foreground="green")
            entry_user.delete(0, tk.END)
            entry_password.delete(0, tk.END)
        else:
            error_msg_label.config(text="Usuario o contraseña no válidos.")
    else:
        error_msg_label.config(text="Usuario existente o opción de recuperación no válida.")


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
style.configure('image.TButton', image=user_image, padding=10, borderwidth=0, background="#F5F5F5")
style.configure('TLabel', background="#F5F5F5", font=("Arial", 18))
style.configure('TEntry', background="#F5F5F5", font=("Arial", 14), borderwidth=0, width=30)

style.configure('secondary.TLabel', font=("Helvetica", 10), foreground="#253346")

style.map('TButton', background=[('active', '#47648B')])


#frames and widgets
# main menu
main_menu = tk.Frame(root, bg="#F5F5F5")

# user_button = ttk.Button(root, style="image.TButton")
welcome_text = ttk.Label(main_menu, text="Bienvenido a la aplicación de mensajes secretos del grupo Dragon")
instructions_text = ttk.Label(main_menu, text="Para continuar, presione el botón 'Continuar' o cierre la ventana.", style='secondary.TLabel')
signup_button = ttk.Button(main_menu, text="Registrarse", command=sign_up_windows)
login_button = ttk.Button(main_menu, text="Iniciar sesión", command=login_windows)
about_text = ttk.Label(main_menu, text="Construida por Facundo Rizzato, ...", font=("Arial", 10))


# signup
signup_menu = tk.Frame(root, bd=5, padx=10, pady=10, bg="#F5F5F5")



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

result_string = tk.StringVar()
result_label = ttk.Label(encryption_menu, text="", font=("Arial", 14))



# Packing
# user_button.pack()
main_menu.pack()
welcome_text.pack(pady=20)
instructions_text.pack(pady=(250, 5))
login_button.pack(pady=10)
signup_button.pack(pady=10)
about_text.pack(pady=20)

#loop
root.mainloop()
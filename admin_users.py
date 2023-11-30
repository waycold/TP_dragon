import tkinter as tk
from tkinter import ttk
import csv
import validation

def recuperacion(user, entry_respuesta, mensaje):
    """Facundo Rizzato
    Verifica si la respuesta ingresada es correcta o no. En caso de ser correcta, muestra la contraseña del usuario.
    """
    with open('resources/data.csv', 'r+', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        lineas = list(lector_csv)

        for fila in lineas:
            if fila[0] == user and fila[3] == entry_respuesta:
                mensaje.config(text=fila[1])
            elif fila[0] == user and int(fila[4]) < 3:
                intentos_restantes = 3 - int(fila[4])
                fila[4] = str(int(fila[4]) + 1)
                mensaje.config(text=f"Respuesta incorrecta. Intentos restantes: {intentos_restantes}")
            else:
                mensaje.config(text="Usuario bloqueado.")

        archivo.seek(0)
        archivo.truncate()
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(lineas)

def recuperacion_button_pressed(user, error_msg, frame_ini, frame_fin, root):
    """Facundo Rizzato
    Valida si el usuario ingresado existe o no. En caso de existir, abre una ventana para recuperar contraseña.
    """
    with open('resources/data.csv', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            if fila[0] == user:
                id_pregunta = fila[2]

    with open('resources/data.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        usuario_encontrado = False

        for fila in lector_csv:
            if fila[0] == user and int(fila[4]) <= 3:
                usuario_encontrado = True
                
                with open('resources/preguntas.csv', newline='', encoding='utf-8') as archivo_csv:
                    lector_csv = csv.reader(archivo_csv)
                    for fila in lector_csv:
                        if fila[0] == id_pregunta:
                            pregunta = fila[1]

                frame_ini.destroy()
                frame_fin.pack()
                
                recuperacion_title = ttk.Label(root, text="Pregunta de recuperación:", style='secondary.TLabel')
                recuperacion_pregunta = ttk.Label(root, text=f"{pregunta}", style='secondary.TLabel')
                recuperacion_entry = ttk.Entry(root, width=50)
                msg_label = ttk.Label(root, text="", foreground="red", style='secondary.TLabel')
                verificar_button = ttk.Button(root, text="Verificar", command=lambda: recuperacion(user, recuperacion_entry.get(), msg_label))

                recuperacion_title.pack(pady=5)
                recuperacion_pregunta.pack(pady=10)
                recuperacion_entry.pack(pady=20)
                msg_label.pack(pady=5)
                verificar_button.pack(pady=10)
                    
            elif fila[0] == user and int(fila[4]) > 3:
                usuario_encontrado = True
                error_msg.config(text="Usuario bloqueado.")
                
        if not usuario_encontrado:
            error_msg.config(text="Usuario incorrectos.")

def login(user, password, error_msg_label, frame, menu):
    """Facundo Rizzato
    Valida si el usuario y contraseña ingresados existen. En caso de ser correctos, abre la ventana de cifrado.
    """
    with open('resources\data.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        
        usuario_encontrado = False
        for fila in lector_csv:
            if fila[0] == user and fila[1] == password:
                usuario_encontrado = True
                if int(fila[4]) <= 3:
                    menu()
                    frame.destroy()
                else:
                    error_msg_label.config(text="Usuario bloqueado.")
                
        if not usuario_encontrado:
            error_msg_label.config(text="Usuario o contraseña incorrectos.")

def registro(user, password, error_msg_label, entry_user, entry_password, recuperacion, recuperacion_options):
    """Facundo Rizzato
    Valida si el usuario ingresado ya existe o no. En caso de no existir, valida si el usuario y contraseña ingresados son válidos.
    En caso de ser válidos, registra el usuario en el archivo data.csv.
    """
    usuario_existente = False
    id_recuperacion = None
    
    with open('resources/data.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if fila[0] == user:
                usuario_existente = True
                error_msg_label.config(text="Usuario ya existente.")
    
    with open('resources/preguntas.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if fila[1] == recuperacion_options:
                id_recuperacion = fila[0]
    
    if not usuario_existente and id_recuperacion is not None:
        if validation.validacion_usuario(user) and validation.validacion_password(password):
            with open('resources/data.csv', 'a', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerow([user, password, id_recuperacion, recuperacion, 0])
    
            error_msg_label.config(text="Usuario registrado correctamente.", foreground="green")
            entry_user.delete(0, tk.END)
            entry_password.delete(0, tk.END)
        else:
            error_msg_label.config(text="Usuario o contraseña no válidos.")
    else:
        error_msg_label.config(text="Usuario existente o opción de recuperación no válida.")

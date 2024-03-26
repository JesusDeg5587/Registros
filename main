# Autor: [Jesus Degollado]
import tkinter as tk
from tkinter import messagebox
import random
import string
import sqlite3
from datetime import datetime
from BaseDatosRegistro import crear_tabla_usuarios, crear_tabla_horarios
import time
llegada_registrada = False
hora_llegada = None
def conectar_base_de_datos():
    conn = sqlite3.connect('Registros.db')
    c = conn.cursor()
    return conn, c
def center_window(window):
    window.update_idletasks()
    width = 400
    height = 200
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
def abrir_ventana_registro(root):
    def registrar_trabajador():
        nombre_apellido = nombre_apellido_entry.get()
        contraseña = contraseña_entry.get()
        confirmar_contraseña = confirmar_contraseña_entry.get()

        if contraseña != confirmar_contraseña:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        if not (any(char.isupper() for char in contraseña) and any(char.isdigit() for char in contraseña)):
            messagebox.showerror("Error", "La contraseña debe contener al menos una mayúscula y un número.")
            return

        id_trabajador = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        agregar_trabajador(nombre_apellido, id_trabajador, contraseña)
        messagebox.showinfo("Registro Exitoso", f"Trabajador registrado correctamente.\nID: {id_trabajador}")
        ventana_registro.destroy()

    ventana_registro = tk.Toplevel(root)
    ventana_registro.title(f"Registrar Trabajador")
    center_window(ventana_registro)

    nombre_apellido_label = tk.Label(ventana_registro, text="Nombre y Apellido:")
    nombre_apellido_label.grid(row=0, column=0, padx=10, pady=5)
    nombre_apellido_entry = tk.Entry(ventana_registro)
    nombre_apellido_entry.grid(row=0, column=1, padx=10, pady=5)

    contraseña_label = tk.Label(ventana_registro, text="Contraseña:")
    contraseña_label.grid(row=1, column=0, padx=10, pady=5)
    contraseña_entry = tk.Entry(ventana_registro, show="*")
    contraseña_entry.grid(row=1, column=1, padx=10, pady=5)

    confirmar_contraseña_label = tk.Label(ventana_registro, text="Confirmar Contraseña:")
    confirmar_contraseña_label.grid(row=2, column=0, padx=10, pady=5)
    confirmar_contraseña_entry = tk.Entry(ventana_registro, show="*")
    confirmar_contraseña_entry.grid(row=2, column=1, padx=10, pady=5)

    registrar_button = tk.Button(ventana_registro, text="Registrar", command=registrar_trabajador)
    registrar_button.grid(row=3, columnspan=2, padx=10, pady=5)

def iniciar_sesion_admin(root):
    def verificar_credenciales():
        if username_entry.get() == "admin" and password_entry.get() == "admin":
            ventana_login.destroy()
            admin_logged_in = True
            abrir_ventana_registro(root)  # Abrir la ventana para registrar trabajadores
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    ventana_login = tk.Toplevel(root)
    ventana_login.title("Iniciar Sesión como Administrador")
    center_window(ventana_login)

    username_label = tk.Label(ventana_login, text="Usuario:")
    username_label.grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(ventana_login)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(ventana_login, text="Contraseña:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(ventana_login, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    login_button = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_credenciales)
    login_button.grid(row=2, columnspan=2, padx=10, pady=5)

def iniciar_sesion_trabajador(root):
    def verificar_credenciales():
        conn, c = conectar_base_de_datos()
        c.execute("SELECT * FROM usuarios WHERE id_trabajador=? AND contraseña=?", (username_entry.get(), password_entry.get()))
        usuario = c.fetchone()
        conn.close()

        if usuario:
            ventana_login.destroy()
            abrir_ventana_registrar_horario(usuario[0])
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    ventana_login = tk.Toplevel(root)
    ventana_login.title("Iniciar Sesión como Trabajador")
    center_window(ventana_login)

    username_label = tk.Label(ventana_login, text="ID Trabajador:")
    username_label.grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(ventana_login)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(ventana_login, text="Contraseña:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(ventana_login, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    login_button = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_credenciales)
    login_button.grid(row=2, columnspan=2, padx=10, pady=5)

def abrir_ventana_registrar_horario(id_trabajador):
    def registrar_llegada():
       global llegada_registrada,hora_llegada
       if not llegada_registrada:
           registrar_horario(id_trabajador, "llegada")
           hora_llegada = time.time()  # Guardar la hora de llegada
           llegada_registrada = True
           messagebox.showinfo("Registro", "Hora de llegada registrada correctamente.")
       else:
           messagebox.showwarning("Advertencia", "La llegada ya ha sido registrada.")

    def registrar_salida():
        global hora_llegada
        if llegada_registrada:
            hora_actual = time.time()
            tiempo_transcurrido = hora_actual - hora_llegada
            if tiempo_transcurrido >= 3600:  # Una hora tiene 3600 segundos
                registrar_horario(id_trabajador, "salida")
                messagebox.showinfo("Registro", "Hora de salida registrada correctamente.")
                llegada_registrada = False  # Reiniciar el estado de llegada
                hora_llegada = None
            else:
                messagebox.showwarning("Advertencia","Debe pasar al menos una hora desde la llegada para registrar la salida.")
        else:
            messagebox.showwarning("Advertencia", "Debe registrar la llegada antes de la salida.")

    ventana_registrar_horario = tk.Toplevel()
    ventana_registrar_horario.title("Registrar Horario")
    center_window(ventana_registrar_horario)

    llegada_button = tk.Button(ventana_registrar_horario, text="Registrar Llegada", command=registrar_llegada)
    llegada_button.grid(row=0, column=0, padx=10, pady=5)

    salida_button = tk.Button(ventana_registrar_horario, text="Registrar Salida", command=registrar_salida)
    salida_button.grid(row=0, column=1, padx=10, pady=5)

def agregar_trabajador(nombre_apellido, id_trabajador, contraseña):
    conn, c = conectar_base_de_datos()
    c.execute("INSERT INTO usuarios (nombre_apellido, id_trabajador, contraseña) VALUES (?, ?, ?)",
              (nombre_apellido, id_trabajador, contraseña))
    conn.commit()
    conn.close()

def registrar_horario(id_trabajador, tipo_registro):
    conn, c = conectar_base_de_datos()
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO horarios (id_trabajador, tipo_registro, fecha_hora) VALUES (?, ?, ?)",
              (id_trabajador, tipo_registro, fecha_hora))
    conn.commit()
    conn.close()


root = tk.Tk()
root.title("Registro de Trabajadores")
center_window(root)

login_admin_button = tk.Button(root, text="Iniciar Sesión como Administrador", command=lambda: iniciar_sesion_admin(root))
login_admin_button.pack(pady=10)

login_trabajador_button = tk.Button(root, text="Iniciar Sesión como Trabajador", command=lambda: iniciar_sesion_trabajador(root))
login_trabajador_button.pack(pady=10)

root.mainloop()

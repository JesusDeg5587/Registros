# Autor: [Jesus Degollado]

import sqlite3
def conectar_base_de_datos():
    conn = sqlite3.connect('Registros.db')
    c = conn.cursor()
    return conn, c

def crear_tabla_usuarios():
    conn, c = conectar_base_de_datos()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    No_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_apellido TEXT NOT NULL,
                    id_trabajador TEXT NOT NULL UNIQUE,
                    contraseña TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

def crear_tabla_horarios():
    conn, c = conectar_base_de_datos()
    c.execute('''CREATE TABLE IF NOT EXISTS horarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_trabajador INTEGER NOT NULL,
                    tipo_registro TEXT NOT NULL,
                    fecha_hora TEXT NOT NULL,
                    FOREIGN KEY (id_trabajador) REFERENCES usuarios(id)
                )''')
    conn.commit()
    conn.close()



# Llamamos a las funciones para crear las tablas
crear_tabla_usuarios()
crear_tabla_horarios()

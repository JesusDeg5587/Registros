# Autor: [Jesus Degollado]

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def conectar_base_de_datos():
    conn = sqlite3.connect('Registros.db')
    c = conn.cursor()
    return conn, c

@app.route('/registros/<id_trabajador>', methods=['GET'])
def obtener_registros(id_trabajador):
    conn, c = conectar_base_de_datos()
    c.execute("SELECT * FROM horarios WHERE id_trabajador=?", (id_trabajador,))
    registros = c.fetchall()
    conn.close()
    return jsonify(registros)

if __name__ == '__main__':
    app.run(debug=True)

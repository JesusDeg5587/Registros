# Autor: [Jesus Degollado]
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sqlite3
from kivy.lang import Builder

Builder.load_string('''
<RootWidget>:
    orientation: 'vertical'
    padding: 20
    spacing: 20

    canvas.before:
        Color:
            rgba: 0.2, 0.2, 0.2, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: root.width*0.8, root.height*0.8
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        Label:
            text: ''
            id: result_label
            halign: 'center'
            valign: 'middle'
            markup: True
            size_hint: None, None
            size: root.width*0.8, 200

        BoxLayout:
            orientation: 'horizontal'
            size_hint: None, None
            size: root.width*0.8, 30
            pos_hint: {'center_x': 0.5}

            TextInput:
                id: id_input
                hint_text: 'ID del trabajador'
                size_hint: None, None
                height: 30
                width: root.width*0.6

            Button:
                text: 'Obtener Registros'
                size_hint: None, None
                height: 40
                width: root.width*0.4
                on_press: app.obtener_registros()
''')

class RegistrosApp(App):
    def build(self):
        return RootWidget()

    def conectar_base_de_datos(self):
        conn = sqlite3.connect('Registros.db')
        c = conn.cursor()
        return conn, c

    def obtener_registros(self):
        id_trabajador = self.root.ids.id_input.text
        conn, c = self.conectar_base_de_datos()
        c.execute("SELECT fecha_hora FROM horarios WHERE id_trabajador=?", (id_trabajador,))
        registros = c.fetchall()
        conn.close()

        formatted_result = "[b]Fechas de Registros:[/b]\n"
        if registros:
            for registro in registros:
                formatted_result += f"{registro[0]}\n"
        else:
            formatted_result += "No se encontraron registros para este ID."

        self.root.ids.result_label.text = formatted_result

class RootWidget(BoxLayout):
    pass

if __name__ == '__main__':
    RegistrosApp().run()

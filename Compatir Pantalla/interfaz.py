import tkinter as tk
from tkinter import ttk
import mariadb


class VentanaNombre(tk.Toplevel):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.callback = callback
        self.config(width=300, height=180)

        self.resizable(0, 0)
        self.title("Ingresa tu nombre")
        # Usuario
        self.caja_nombre = ttk.Entry(self)
        self.caja_nombre.place(x=20, y=20, width=260)
        # Contrasenha
        self.caja_password = ttk.Entry(self, show="*")
        self.caja_password.place(x=20, y=50, width=260)
        # Boton listo
        self.boton_listo = ttk.Button(
            self,
            text="¡Listo!",
            command=self.boton_listo_presionado
        )
        self.boton_listo.place(x=20, y=80, width=260)
        self.focus()
        self.grab_set()

    def boton_listo_presionado(self):
        self.callback(self.caja_nombre.get(), self.caja_password.get())
        self.destroy()


class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("Ventana principal")
        self.boton_solicitar_nombre = ttk.Button(
            self,
            text="Solicitar nombre",
            command=self.solicitar_nombre
        )
        self.boton_solicitar_nombre.place(x=50, y=50)
        self.etiqueta_nombre = ttk.Label(
            self,
            text="Aún no has ingresado ningún nombre."
        )
        self.etiqueta_nombre.place(x=50, y=150)

    def solicitar_nombre(self):
        self.ventana_nombre = VentanaNombre(
            callback=self.nombre_ingresado
        )

    def nombre_ingresado(self, nombre, password):
        self.etiqueta_nombre.config(
            text="Ingresaste el nombre: " + nombre
        )
        
        cone = self.abrir(nombre, password)
        cursor = cone.cursor()
        sql = "select * from estudiantes where id=21"
        cursor.execute(sql)
        return cursor.fetchall()

    def abrir(self, user, password):
        try:
            conexion = mariadb.connect(user=user,
                                    password=password,
                                    host="186.64.121.140",
                                    database="utrack")
            return conexion
        except KeyError as e:
            print(e)
            

    def listar(self):
        respuesta = self.nombre_ingresado()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(self, "código:"+str(fila[0]) +
                                              "\ndescripción:"+fila[1] +
                                              "\nprecio:"+str(fila[2])+"\n\n")


ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()

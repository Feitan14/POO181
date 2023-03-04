import tkinter as tk
from login import *

class Ventana(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Practica 12: Login")
        self.geometry("600x400")
        #Etiqueta de email
        self.email_label = tk.Label(text="Correo electrónico:")
        self.email_label.pack()
        #Entry de email
        self.entryem = tk.Entry(self)
        self.entryem.pack()
        #Etiqueta de contraseña
        self.password_label = tk.Label(text="Contraseña:")
        self.password_label.pack()
        #Entry de contraseña con *
        self.password_entry = tk.Entry(show="*")
        self.password_entry.pack()
        #Boton de ingresar con la funcion de obtener los datos de los entry's, y mandarlos a la clase login
        self.button = tk.Button(self, text="Ingresar", command=self.on_button)
        self.button.pack()
        
    #Función para el botón
    def on_button(self):
        #se crea el objeto con los gets de los entry's
        verif=diego(self.entryem.get(),self.password_entry.get())
        #se mandan los parametros de los gets para la funcion loginveriicacion de la clase login.py
        verif.loginVerificacion()

ventana = Ventana()
ventana.mainloop()
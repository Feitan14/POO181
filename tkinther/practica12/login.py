from tkinter import messagebox

class diego:
    def __init__(self, em,passw):
        self.__email=em
        self.__password=passw


    def loginVerificacion(self):
        if self.__email == "" or self.__password == "":
            messagebox.showerror("Error Vacio","Por favor ingrese su correo y contraseña, el campo no puede quedar vacio ")
        elif self.__email == "1" and self.__password == "2":
            messagebox.showinfo("¡Bienvenido!","Acceso permitido")
        else:
            messagebox.showwarning("Error","El correo o la contraseña son incorrectos")
                

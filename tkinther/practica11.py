from tkinter import Tk,Frame,Button,messagebox

#4. Función de mensajes.
def mostrarMensaje():
    messagebox.showinfo("Aviso","Este mensaje es información")
    messagebox.showerror("Error:","todo fallo con exito")
    print(messagebox.ask("pregunta:", "El o ella jugó con tu corazon"))
    
    
#5. funcion para agregar botones

def agregarBoton():
    BotonVerde.config(text="+",bg="green",fg="white")    
    botonNuevo = Button(seccion3,text="boton nuevo")
    botonNuevo.pack()
    
#1. creación ventana


#instancia
Ventana = Tk()

Ventana.title("Practica 11:3 frame")
Ventana.geometry("600x400")

#2. Definir las secciones de la ventana 
seccion1=Frame(Ventana,bg="#990099")
seccion1.pack(expand = True, fill='both')

seccion2=Frame(Ventana,bg="#0000ff")
seccion2.pack(expand = True, fill='both')

seccion3=Frame(Ventana,bg="#660033")
seccion3.pack(expand = True, fill='both')

#3. boton azul 

botonAzul=Button(seccion1,text="boton azul",fg="blue",command=mostrarMensaje)
botonAzul.place(x=60,y=60)

botonamarillos=Button(seccion2,text="boton amarillo",fg="white", bg="black")
botonamarillos.grid(row=0, column=0)

BotonNegro=Button(seccion2,text="boton azul",fg="red")
BotonNegro.grid(row=1, column=1)

BotonVerde=Button(seccion3, text="boton verde",bg="green",fg="white", command=agregarBoton)
BotonVerde.pack()


#Main ejecución de la ventana 
Ventana.mainloop()
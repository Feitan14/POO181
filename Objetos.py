#1. importar la clase

from personaje import *

#2. Solicitar atributos para el objeto

print("")
print("### Solicitud de datos heroe ###")
espH = input("Escribe la especie del heroe  ")
nomH = input("Escribe el nombre del heroe  ")
altH = float(input("Escribe la altura del heroe  "))
cargaH = int(input("Cuantas balas se recargaran el heroe  "))


print("")
print("### Solicitud de datos heroe ###")
espV = input("Escribe la especie del villano  ")
nomV = input("Escribe el nombre del villano  ")
altV = float(input("Escribe la altura del villano  "))
cargaV = int(input("Cuantas balas se recargaran el villano  "))

#3. Creamos dos objetos

Heroe=Personaje(espH,nomH,altH)
Villano = Personaje(espV,nomV,altV)

#4. Instanciar un objeto 


#5. Acceder a sus atributos

print("atributos y metodos del heroe: ")

print("El personaje pertenece a la raza " + Heroe.especie)

print("El personaje se llama " + Heroe.nombre)

print("El personaje mide  "+ str(Heroe.altura) + " metros")

print("metodos")

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)

print("atributos y metodos del villano: ")

print("El personaje pertenece a la raza " + Villano.especie)

print("El personaje se llama " + Villano.nombre)

print("El personaje mide  "+ str(Villano.altura) + " metros")

print("metodos")

Villano.correr(True)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)
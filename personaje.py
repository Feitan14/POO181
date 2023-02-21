class Personaje: 
    
    #atributos del personaje
    
    especie = "Humano"
    nombre = "Reyna" 
    altura = 1.90
    
    #metodos del personaje
    
    def correr(self, status):
        if(status):
            print("el personaje " + self.nombre + " está corriendo ")
        else:
            print("el personaje " + self.nombre + " se detuvo")
            
    def lanzarGranada(self):
        print("Se lanzó Granada")
    
    def recargarArma(self,municiones):
        cargador=5 
        cargador=cargador+municiones
        
        print("El arma tiene ahora " + cargador +"balas")
    
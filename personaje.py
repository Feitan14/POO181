class Personaje: 
    
    
    #atributos del personaje
    def __init__(self, esp,nom,alt):
        
        especie = esp
        nombre = nom   
        altura = alt
        self.especie = especie
        self.nombre = nombre
        self.altura = altura
    

    
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
        
        print("El arma tiene ahora " + str(cargador) + " balas")
    
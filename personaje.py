class Personaje: 
    
    
    #atributos del personaje
    def __init__(self, esp,nom,alt):
        
       # especie = esp
       #nombre = nom   
       # altura = alt
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
    

    
    #metodos del personaje
    
    def correr(self, status):
        if(status):
            print("el personaje " + self.__nombre + " está corriendo ")
        else:
            print("el personaje " + self.__nombre + " se detuvo")
            
    def lanzarGranada(self):
        print("Se lanzó Granada")
    
    def recargarArma(self,municiones):
        cargador=5 
        cargador=cargador+municiones
        
        print("El arma tiene ahora " + str(cargador) + " balas")
        
    def __pensar(self):
        print("toy pensando")
        
        
    def getEspecie(self):
        return self.__especie
    def setEspecie(self,esp):
        self.__especie=esp
        
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nom):
        self.__nombre=nom
    
    def getAltura(self):
        return self.__altura
    def setAltura(self,alt):
        self.__altura=alt
    
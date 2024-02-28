class Persona:
    def __init__(self, nombre, anos):
        self.anos = anos 
        self.nombre = nombre
        
        
    def imprimir(self):
        print(self.nombre, "tiene" ,self.anos, "años")
        
        
        
        
    def cumpleanos(self):
        self.anos += 1
        self.imprimir()
        
        
if __name__ == "__main__":
    obama = Persona("Obama", 62)
    obama.imprimir()
    obama.cumpleanos()
    
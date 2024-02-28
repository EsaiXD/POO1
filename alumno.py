class alumno:
    def __init__(self):
        self.nota = 0 
        self.nombre = ""
    
    
    def imprimir(self):
        self.nota = 0
        self.nombre = ""
        print(self.nombre, "obtiene" ,self.nota)
        
        
    def promociona(self):
        if (self.nota >= 5):
            print("promociona")
            
        else:
            print("no promociona")
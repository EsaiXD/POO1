class alumno:
    
    
    def imprimir(self):
        self.nota = 0
        self.nombre = ""
        print(self.nombre, "obtiene" ,self.nota)
        
        
    def promociona(self):
        self.nota = 0
        self.nombre = ""
        if (self.nota >= 5):
            print("promociona")
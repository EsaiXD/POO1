class Calculo:
    def __init__(self, numero1:int, numero2:int):
        self.numero1 = numero1
        self.numero2 = numero2
        
        
    def suma(self):
       return self.numero1 + self.numero2
        
        
    def resta(self):
        return self.numero1 + self.numero2
    
    
    def multiplicacion(self):
        return self.numero1 * self.numero2
    
    
    def division(self):
        if self.numero2 == 0:
            return "Error"
        else: 
            return self.numero1 / self.numero2
        
if __name__ == "__main__":
   calculadora = Calculo(10, 5)
   print("Suma:", calculadora.suma())
   print("Resta:", calculadora.resta())
   print("Multiplicación:", calculadora.multiplicacion())
   print("Division:", calculadora.division())
   


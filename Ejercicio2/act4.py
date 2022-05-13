class Operaciones():
    def __init__(self):      
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0

        
    def suma(self):
        self.resultado = self.num1 + self.num2
        print("Suma: ", self.resultado)

    def resta(self):
        self.resultado = self.num1 - self.num2
        print("Resta: ", self.resultado)

    def multiplicacion(self):
        self.resultado = self.num1 * self.num2
        print("Multiplicacion: ", self.resultado)

    def division(self):
        try:
            self.resultado = self.num1 / self.num2
            print("Division: ", self.resultado)
        except:
            print("Division: no se puede dividir por 0")

operaciones = Operaciones()
operaciones.num1 = int(input("Ingrese el primer numero: "))
operaciones.num2 = int(input("Ingrese el segundo numero: "))
print("\n")
operaciones.suma()
operaciones.resta()
operaciones.multiplicacion()
operaciones.division()
print("\n")
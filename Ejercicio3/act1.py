#Ejercicio 1
class Operaciones():
    def Carga(self):
        self.num1 = int(input("Ingrese el primer numero: "))
        self.num2 = int(input("Ingrese el segundo numero: "))
    def Suma(self):
        self.resultado = self.num1 + self.num2
        print("El resultado de la suma es: ", self.resultado)

    def Pedir(self):
        self.pedir = input("Desea realizar otra operacion? (S/N): ")
        try:
            if self.pedir == "S":
                self.carga()
                self.suma()
                self.pedir()
            elif self.pedir == "N":
                print("Gracias por utilizar el programa")
            else:
                print("Opcion no valida")
                self.pedir()
        except:
            print("Operacion denegada")

opraciones = Operaciones()
opraciones.Carga()
opraciones.Suma()
opraciones.Pedir()


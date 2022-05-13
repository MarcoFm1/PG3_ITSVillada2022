class Persona:
    def atributos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Su nombre es:", self.nombre, "y tiene", self.edad, "años")

class Empleado(Persona):
    def atributos(self, sueldo):
        super().atributos(sueldo)
        self.sueldo = sueldo

    def sueldo(self):
        salario = int(input("Ingrese el sueldo de Pepe: "))
        self.sueldo = salario

    def impuesto(self):
        if self.sueldo > int(3000):
            print("El empleado debe pagar impuestos debido a su alto salario")
        else:
            print("Esta libre de deudas")


    def imprimir(self):
        print("Sueldo: ", self.sueldo)
        self.impuesto()

person = Persona()
person.atributos("Pepe", 22)
empleado = Empleado()
empleado.sueldo()
empleado.impuesto()
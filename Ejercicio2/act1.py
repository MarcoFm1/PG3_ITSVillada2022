class Persona():
    def setName(self):
        self.nombre = str(input("Ingrese su nombre: "))

    def getNombre(self):
        return self.nombre

persona1 = Persona()
persona1.setName()
print("El nombre de la persona es: ", persona1.getNombre())
        
class Alumno():
    def nombreAlumno(self):
        self.nombre = str(input("Ingrese el nombre del alumno: "))
        return self.nombre
    
    def notasAlumno(self):
        self.notas = []
        for i in range(3):
            self.notas.append(int(input("Ingrese la nota del alumno: ")))
        return self.notas

    def promedioAlumno(self):
        self.promedio = sum(self.notas) // len(self.notas)
        if self.promedio >= 6:
            print("El alumno aprobó")
        else:
            print("El alumno reprobó")
        return self.promedio

    def imprimirAlumno(self):
        print("Nombre: ", self.nombre)
        print("Notas: ", self.notas)
        print("Promedio: ", self.promedio)

print("\n")
print("=================")

alum = Alumno()
alum.nombreAlumno()
alum.notasAlumno()
alum.promedioAlumno()
alum.imprimirAlumno()
print("\n")

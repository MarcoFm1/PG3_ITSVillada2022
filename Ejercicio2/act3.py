class Triangulo():
    def __init__(self):
        self.lado1 = 0
        self.lado2 = 0
        self.lado3 = 0
        self.tipo = ""

    def lados(self):
        lista = []
        self.lado1 = int(input("Ingrese el primer lado: "))
        self.lado2 = int(input("Ingrese el segundo lado: "))
        self.lado3 = int(input("Ingrese el tercer lado: "))
        lista.append(self.lado1)
        lista.append(self.lado2)
        lista.append(self.lado3)
        print("Lados: ", lista)

    def tipoTriangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            self.tipo = "Equilatero"
        elif self.lado1 != self.lado2 != self.lado3 != self.lado1:
            self.tipo = "Escaleno"
        else:
            self.tipo = "Isoceles"

    def masGrande(self):
        lista = []
        lista.append(self.lado1)
        lista.append(self.lado2)
        lista.append(self.lado3)
        lista.sort()
        print("Lado mas grande: ", lista[2])

    def imprimirTriangulo(self): 
        print("Tipo de triangulo: ", self.tipo)
    
triangulo = Triangulo()
print("fan lover de EULA uwu esos 30 cm de cadera son exqisitos uwuwuwuwuwuwuwuuw. By:")
triangulo.lados()
triangulo.tipoTriangulo()
triangulo.masGrande()
triangulo.imprimirTriangulo()
print("\n")
    
    #fan lover de EULA uwu esos30 cm de cadera son exqisitos uwuwuwuwuwuwuwuuw

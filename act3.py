print("====EJERCICIO N°4====")

width  = int(input("Ancho = "))
height = int(input("Largo = "))
letter = str(input("Ingrese un caracter = "))
for i in range(height):
    for X in range(width):
        print(letter , end=" ")
    print()
print("The program has been ejecutad")

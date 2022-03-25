print("====EJERCICIO N°4====")
def pintar():
    for i in range(height):
        
        print(str(letter)*width)
width  = int(input("Ancho = "))
height = int(input("Alto = "))
letter = str(input("Ingrese un caracter = "))


pintar()
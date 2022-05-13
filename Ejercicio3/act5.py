#Ejercicio 5

from copyreg import add_extension


archivo = open("./Ejercicio3/AAA.txt", "w")
def ej1():
    Bucle = True
    while Bucle:
        try:
            dato1 = str(input("String: "))
            dato2 = int(input("Int: "))

            archivo.write(dato1)
            archivo.write(" / mensaje guardado\n")

            archivo.write(dato2)
            archivo.write(" / mensaje guardado\n")
        except ValueError:
            print("Se ingreso un valor no valido")
        except TypeError:
            print("{dato1} Se guardo en el txt")
            archivo.close()
        
ej1()
archivo.close()
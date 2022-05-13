#Ejercicio 2


def Ejercicio2():
    while True:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        try:
            print("La division entre esos numeros es: ", num1 // num2)
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
        except ValueError:
            print("El valor ingresado no es valido")
Ejercicio2()




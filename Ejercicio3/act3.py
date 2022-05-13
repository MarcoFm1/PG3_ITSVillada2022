#Ejercicio 3
month = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
def Meses():
    while True:
        try:
            num = int(input("Ingrese el numero del mes: "))
            if num > 0 and num < 13:
                print(month[num - 1])
            else:
                print("El numero ingresado no es valido")
        except IndexError:
            print("El numero valor no es valido")

Meses()
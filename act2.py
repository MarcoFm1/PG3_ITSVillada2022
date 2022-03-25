print("====EJERCICIO N°2====")

while True:
    yr = int(input("Ingrese un año: "))

    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
            print (yr, "Este es un año bisiesto UwU")
    else:
            print (yr, "Tristemente no un año bisiesto UnU")


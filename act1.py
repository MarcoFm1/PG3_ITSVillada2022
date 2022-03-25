import random
import time
print("====EJERCICIO N°1====")
while True:
    num_ran = [random.randint(0, 99) for x in range(5)]
    print("Generando lista aleatoria...")
    time_duration = 2
    time.sleep(time_duration)
    print("Tu lista generada: " ,num_ran)

    srch = int(input("Ingrese el numero que desee buscar: "))
    def buscar(num_ran, srch):
        try:
            print(num_ran.index(srch))
        except:
            print("No hay.")
    
    buscar(num_ran, srch)

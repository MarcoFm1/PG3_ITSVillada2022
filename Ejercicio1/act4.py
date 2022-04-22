import random
import time
print("====EJERCICIO N°4")

def bubble_sort(list1):  
    
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
  
list1 = [random.randint(0, 99) for x in range(5)]
print("Generando lista aleatoria...")
time_duration = 2
time.sleep(time_duration)
print("Tu lista generada sin ordenar: " ,list1)
print("La lista ordenada: ", bubble_sort(list1)) 

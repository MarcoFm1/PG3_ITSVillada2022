from ast import While
from cmath import pi

def menu():
    while True:
        print("Choose an action: ")
        e = int(input("➢ Press " + "1 "+ "to do a SQUARE\n➢ Press "+"2 "+"to do a TRIANGLE\n➢ Press 3 to do a STAR\n"))
        if(e==1):
            print("YOU'RE DOING A SQUARE")
            pintar()
            print("\n" * 2)

        if(e==2):
            print("YOU'RE DOING A TRIANGLE")
            triangle()
            print("\n" * 2)
        
        if(e==3):
            print("YOU'RE DOING A STAR")
            print("\n" * 2)



def pintar():
    width  = int(input("Ancho = "))
    height = int(input("Alto = "))
    letter = str(input("Ingrese un caracter = "))
    for i in range(height):
        
        print(str(letter)*width)
        print("\n" * 2)


def triangle():
    rows = int(input("Ingrese el número de filas: "))
    c = str(input("Ingrese el caracter para hacer tu piramide: "))
    r = 0
    for i in range(1, rows+1):
        for space in range(1, (rows-i)+1):
            print(end="  ")
    
        while r!=(2*i-1):
            print(c, "", end="")
            r += 1
        r = 0
        print()
    print("\n" * 2)


menu()




    



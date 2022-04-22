print("====EJERCICIO N°5====")
def palindromo():
    word = str(input("Escribe una palabra: "))
    if str(word) == str(word)[::-1] :
        print("Esta palabra es un palíndromo")
    else:
        print("No es un palíndromo UnU")

palindromo()



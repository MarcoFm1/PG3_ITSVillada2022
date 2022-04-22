import time

def Vocal(frase):
    vocals = 'aeiouAEIOU'
    return set ([c for c in frase if c in vocals])

sen = str(input("Introduce una frase: "))
print("Analizando tu frase....")
time_duration = 2
time.sleep(time_duration)
print(Vocal(sen))
print(("Tu frase tiene "), len(Vocal(sen)), (" vocales."))

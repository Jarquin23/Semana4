#adivinar un numero
import random
numero_secreto = random.randint(1, 10)
numero_usuario = int(input("Dime un número del 1 al 10: "))
print(numero_secreto)
if(numero_secreto == numero_usuario):
    print("Felicidades, adivinaste el numero secreto.")
else:
    print("Sigue intentando bro.")
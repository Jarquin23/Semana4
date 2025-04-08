#Calcular la edad actual y la edad dentro de 10 años
año_nac = int(input("Ingrese su año de nacimiento: "))
año_act = int(input("Ingrese el año actual: "))
edad_act = año_act - año_nac
edad_fut = edad_act + 10
print(f"Su edad actual es de {edad_act}")
print(f"Su edad dentro de 10 años será de {edad_fut}")
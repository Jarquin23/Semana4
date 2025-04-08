#Calcular el porcentaje de un número dado
num = float(input("Ingrese un número: "))
por = float(input("Ingrese el porcentaje a calcular: "))
resultado = (por / 100) * num
print(f"El {por}% de {num} es: {resultado}")
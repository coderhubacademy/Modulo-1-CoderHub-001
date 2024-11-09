# Recibir 3 notas y calcular el promedio

#version 1

nota1 = 15
nota2 = 20
nota3 = 10

nota_final = (nota1 + nota2 + nota3) / 3

print("La nota final es:", nota_final)

#version 2

nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
nota3 = int(input("Ingrese la nota 3: "))

nota_final = (nota1 + nota2 + nota3) / 3

print("La nota final es:", nota_final)

# Recibir el precio de un producto y restarle un porcentaje de descuento fijo

#version 1

descuento = 20
precio = int(input("Ingrese el precio del producto: "))

precio_final = precio - (precio * (descuento / 100))
print("El precio final es:", precio_final)

#version 2

# descuento = float(input("Ingrese el descuento: "))
# price = float(input("Ingrese el precio del producto: "))

# precio_descuento = price * descuento
# price_final = price - precio_descuento

# print("El precio final es:", price_final)


# Calcular grados Celsius a Fahrenheit

#version 1

celsius = 37
fr = (celsius * 9/5) + 32

print("La temperatura en Fahrenheit es:", fr)
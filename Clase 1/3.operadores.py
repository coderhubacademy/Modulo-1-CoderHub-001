#Operadores: Aritmeticos, Relacionales, Logicos, Asignacion, Especiales

"""Los operadores son sımbolos especiales que representan cálculos y acciones
sobre variables y valores. 
Los operadores aritméticos se utilizan para realizar
operaciones matemáticas. 
Los operadores relacionales se utilizan para comparar
valores. 
Los operadores lógicos se utilizan para combinar expresiones
condicionales. 
Los operadores de asignación se utilizan para asignar valores a
variables. 
Los operadores especiales se utilizan para realizar operaciones
especiales, como la concatenación de cadenas."""

# Operadores Aritmeticos

# Suma (+)
# Resta (-)
# Multiplicacion (*)
# Division (/)
# Modulo (%)
# Potencia (**)

suma = 5 + 3
print("Suma", suma)
resta = 5 - 3
print("Resta", resta)
multiplicacion = 5 * 3
print("Multiplicacion", multiplicacion)
division = 5 / 3
print("Division", division)
modulo = 5 % 3
print("Modulo", modulo)
potencia = 5 ** 3
print("Potencia", potencia)

suma_total = suma + resta + multiplicacion + division + modulo + potencia

print("Suma Total", suma_total)

# Convertir suma_total a un entero
suma_total = int(suma_total)
print("Suma Total Convertida", suma_total)

# Operadores Relacionales

# Mayor que (>)
# Menor que (<)
# Mayor o igual que (>=)
# Menor o igual que (<=)
# Igual que (==)
# Diferente que (!=)

a = 5
b = 3

print("a > b ->", a > b)

nombre_david = "David"
nombre_francisco = "Francisco"

print("nombre_david == nombre_francisco ->", nombre_david == nombre_francisco)
print("nombre_david != nombre_francisco ->", nombre_david != nombre_francisco)

# Operadores Logicos

# and
# or
# not

# and - Solo es verdadero si ambos valores son verdaderos
# or - Es verdadero si uno de los valores es verdadero
# not - Es verdadero si el valor es falso

nombre_1 = "David"
sexo_1 = "M"
edad_1 = 25

nombre = "Eva"
sexo = "F"
edad = 60

condicion_1 = sexo_1 == "M" and edad_1 > 60
print("condicion_1", condicion_1)

condicion_2 = sexo == "F" and edad > 55
print("condicion_2", condicion_2)

fruta1 = "Tomate"
fruta2 = "Pera"

condicion_3 = fruta1 == "Manzana" or fruta2 == "Manzana"
print("condicion_3", condicion_3)

nombre = "David"

condicion_4 = not nombre == "David"
print("condicion_4", condicion_4)

# Operadores de Asignacion

# = Asignacion
# += Suma y asigna
# -= Resta y asigna
# *= Multiplica y asigna
# /= Divide y asigna
# %= Modulo y asigna
# **= Potencia y asigna

a = 5
b = 3
c = 10

c += a + b
print("c", c)

c -= a
print("c con resta", c)
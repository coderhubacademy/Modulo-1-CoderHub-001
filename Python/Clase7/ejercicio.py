personas = [{'nombre': 'Juan', 'edad': 35}, 
            {'nombre': 'María', 'edad': 25}, 
            {'nombre': 'Pedro', 'edad': 40},
            {'nombre': 'Luis', 'edad': 30},
            {'nombre': 'Ana', 'edad': 20},
            {'nombre': 'Carlos', 'edad': 15},
            {'nombre': 'Luisa', 'edad': 50},
            {'nombre': 'Jorge', 'edad': 55},
            {'nombre': 'Elena', 'edad': 10},
            {'nombre': 'Carmen', 'edad': 65}]
# print(personas)
# print(len(personas))

ninos = []
adultos = []
ancianos = []

for persona in personas:
    if persona['edad'] < 18:
        ninos.append(personas)
    elif persona['edad'] >= 18 and persona['edad'] < 65:
        adultos.append(persona)
    else:
        ancianos.append(persona)
        
print("Niños", ninos, "\n")
print("Adultos", adultos, "\n")
print("Ancianos", ancianos, "\n")

# promedio de edad de personas

suma = 0
for persona in personas:
  suma += persona['edad']
    
promedio = suma / len(personas)

print("El promedio de edad de las personas es:", promedio)
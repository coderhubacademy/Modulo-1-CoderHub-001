class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

animales = [Perro(), Gato()]
for animal in animales:
    print(animal.hablar())  # polimorfismo
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        if self.species.lower() == "cat":
            return "Мяу!"
        elif self.species.lower() == "dog":
            return "Гав!"
        else:
            return "Невідомий звук"

    def eat(self, food):
        return f"{self.name} їсть {food}."

    def sleep(self, hours):
        return f"{self.name} спить {hours} годин."

pet1 = Pet("Віскі", "cat")
print(pet1.speak())
print(pet1.eat("риба"))
print(pet1.sleep(5))

pet2 = Pet("Рекс", "dog")
print(pet2.speak())
print(pet2.eat("кість"))
print(pet2.sleep(3))

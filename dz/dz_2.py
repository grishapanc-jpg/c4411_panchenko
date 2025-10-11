class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 50

    def speak(self):
        if self.species.lower() == "cat":
            return "Мяу!"
        elif self.species.lower() == "dog":
            return "Гав!"
        else:
            return "..."

    def play(self):
        if self.energy > 10:
            self.energy -= 10
            return f"{self.name} грається. Рівень енергії: {self.energy}"
        else:
            return f"{self.name} втомився і хоче спати."

    def sleep(self):
        self.energy += 20
        if self.energy > 100:
            self.energy = 100
        return f"{self.name} спить. Енергія зараз: {self.energy}"

    def eat(self, food):
        self.energy += 15
        if self.energy > 100:
            self.energy = 100
        return f"{self.name} їсть {food}. Енергія: {self.energy}"


class Human:
    def __init__(self, name):
        self.name = name
        self.mood = 50

    def feed_pet(self, pet, food):
        print(f"{self.name} годує {pet.name}.")
        print(pet.eat(food))
        self.mood += 5

    def play_with_pet(self, pet):
        print(f"{self.name} грається з {pet.name}.")
        print(pet.play())
        self.mood += 10

    def rest(self):
        self.mood += 10
        if self.mood > 100:
            self.mood = 100
        print(f"{self.name} відпочиває. Настрій: {self.mood}")

    def status(self):
        return f"{self.name} має настрій: {self.mood}"



pet = Pet("Бім", "dog")
person = Human("Оксана")

print(person.status())
person.feed_pet(pet, "кістку")
person.play_with_pet(pet)
print(pet.sleep())
person.rest()
print(person.status())

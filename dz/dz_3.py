class Animal:
    def __init__(self, name):
        self.name = name
        self.species = "Не визначено"

    def speak(self):
        return f"{self.name} робить звук."

    def info(self):
        return f"Це {self.species} на ім'я {self.name}."



class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.species = "Собака"
        self.breed = breed

    def speak(self):
        return f"{self.name} каже: Гав!"

    def info(self):
        return f"{super().info()} Це порода: {self.breed}."



class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.species = "Кіт"
        self.color = color

    def speak(self):
        return f"{self.name} каже: Мяу!"

    def info(self):
        return f"{super().info()} Це колір: {self.color}."



dog = Dog("Рекс", "Німецька вівчарка")
cat = Cat("Барсик", "Чорний")

print(dog.speak())
print(dog.info())

print(cat.speak())
print(cat.info())

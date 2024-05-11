class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class Bird(Animal):
    def speak(self):
        return f"{self.name} says Chirp!"


def make_animal_speak(animal):
    return animal.speak()


my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")
my_bird = Bird("Tweetie")

print(make_animal_speak(my_dog))
print(make_animal_speak(my_cat))
print(make_animal_speak(my_bird))

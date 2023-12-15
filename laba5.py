from enum import Enum

class Kind(Enum):
    dog = 1
    cat = 2
    bird = 3
    parrot = 4

class Pet():


    def isPolite(self):
        return "Hello" in self.greeting or "hello" in self.greeting

    def __str__(self):
        return f"{self.name} ({self.kind.name}) - {self.age} years old"

class Home():
    def __init__(self):
        self.pets = []

    def addPet(self, pet):
        self.pets.append(pet)

    def areFriends(self, pet1, pet2):
        return abs(pet1.age - pet2.age) <= 2

    def sortPetsByAge(self):
        self.pets.sort(key=lambda pet: pet.age)

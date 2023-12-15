from laba5 import Kind
from laba5 import Pet
from laba5 import Home

if __name__ == "__main__":
    dog1 = Pet("bobik", "Retriever", 8, "Hello gaf-gaf", 25, Kind.dog)
    cat1 = Pet("kisa", "Siamese", 2, "Meow-Meow", 8, Kind.cat)
    bird1 = Pet("kiwik", "kiwi", 1, "ci-ci-ci", 0.01, Kind.bird)
    parrot1 = Pet("bigbob", "KingParrot", 4, "hello", 1, Kind.parrot)

    home = Home()
    home.addPet(dog1)
    home.addPet(cat1)
    home.addPet(bird1)
    home.addPet(parrot1)

    for pet in home.pets:
        if pet.isPolite():
            print(f"{pet.name} is polite.")
        else:
            print(f"{pet.name} is not polite.")

    home.sortPetsByAge()
    print("Pets sorted by age:")
    for pet in home.pets:
        print(f"{pet.name} - {pet.age} years old")

    print("Friends:")
    for i in range(len(home.pets)):
        for j in range(i + 1, len(home.pets)):
            if home.areFriends(home.pets[i], home.pets[j]):
                print(f"{home.pets[i].name} and {home.pets[j].name} are friends.")

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):
        if animal.species == "dog":
            self.dogs.append(animal)
        elif animal.species == "cat":
            self.cats.append(animal)

    def dequeue(self, pref):
        if pref == "dog" and self.dogs:
            return self.dogs.pop(0)
        elif pref == "cat" and self.cats:
            return self.cats.pop(0)
        else:
            return None

if __name__ == "__main__":
    shelter = AnimalShelter()

    dog1 = Animal("dog", "Buddy")
    dog2 = Animal("dog", "Max")
    cat1 = Animal("cat", "Fluffy")
    cat2 = Animal("cat", "Whiskers")

    shelter.enqueue(dog1)
    shelter.enqueue(cat1)
    shelter.enqueue(dog2)
    shelter.enqueue(cat2)

    print(shelter.dequeue("dog").name)  # Output: Buddy
    print(shelter.dequeue("cat").name)  # Output: Fluffy
    print(shelter.dequeue("dog").name)  # Output: Max
    print(shelter.dequeue("cat").name)  # Output: Whiskers
    print(shelter.dequeue("dog"))       # Output: None (No more dogs in the shelter)

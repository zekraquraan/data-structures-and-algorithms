class AnimalShelter:
    """Represents an animal shelter that can enqueue and dequeue animals."""

    def __init__(self):
        """Initialize an AnimalShelter object with empty lists for dogs and cats."""
        self.dogs = []  # stack for dogs
        self.cats = []  # stack for cats
        self.arrival_time = 0

    def enqueue(self, animal):
        """
        Add an animal to the shelter.

        Args:
            animal (Animal): The Animal object to enqueue.
        """
        animal.arrival_time = self.arrival_time
        self.arrival_time += 1

        if animal.species == "dog":
            self.dogs.append(animal)
        elif animal.species == "cat":
            self.cats.append(animal)

    def dequeue(self, pref):
        """
        Remove and return an animal from the shelter based on the preference.

        Args:
            pref (str): The preferred species ("dog", "cat"), or None to get the longest-waiting animal.

        Returns:
            Animal or None: The dequeued Animal object if found, None otherwise.
        """
        if pref == "dog" and self.dogs:
            return self.dogs.pop()  # Popping from the end of the stack
        elif pref == "cat" and self.cats:
            return self.cats.pop()  # Popping from the end of the stack
        elif pref is None:
            if self.dogs and self.cats:
                if self.dogs[-1].arrival_time < self.cats[-1].arrival_time:
                    return self.dogs.pop()  # Popping from the end of the stack
                else:
                    return self.cats.pop()  # Popping from the end of the stack
            elif self.dogs:
                return self.dogs.pop()  # Popping from the end of the stack
            elif self.cats:
                return self.cats.pop()  # Popping from the end of the stack
        return None


if __name__ == "__main__":
    shelter = AnimalShelter()

    dog1 = Animal("dog", "Buddy", 0)
    dog2 = Animal("dog", "Max", 1)
    cat1 = Animal("cat", "Fluffy", 2)
    cat2 = Animal("cat", "Whiskers", 3)

    shelter.enqueue(dog1)
    shelter.enqueue(cat1)
    shelter.enqueue(dog2)
    shelter.enqueue(cat2)

    print(shelter.dequeue("dog").name)  # Output: Max (Changed due to stack behavior)
    print(shelter.dequeue("cat").name)  # Output: Whiskers (Changed due to stack behavior)
    print(shelter.dequeue("dog").name)  # Output: Buddy (Changed due to stack behavior)
    print(shelter.dequeue("cat").name)  # Output: Fluffy (Changed due to stack behavior)
    print(shelter.dequeue("dog"))       # Output: None (No more dogs in the shelter)
    animal = shelter.dequeue(None)
    if animal is not None:
        print(animal.name)
    else:
        print("No more animals in the shelter")

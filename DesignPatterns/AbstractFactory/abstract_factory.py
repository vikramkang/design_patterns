class Dog:

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food"

class  Cat:

    def speak(self):
        return "Meaow!"

    def __str__(self):
        return "Cat"


class CatFactory:

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Cat Food"
class PetStore:
    """Pet store houses the abstract factory"""

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display details of the objects returned"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is {}".format(pet))
        print("Our pet says {}".format(pet.speak()))
        print("Our pet food is {}".format(pet_food))


if __name__ == "__main__":
    # Create the concrete factory
    factory = DogFactory()

    # Create the pet store housing abstract factory
    shop = PetStore(factory)

    # Invoke the utility method to show details of our pet
    shop.show_pet()

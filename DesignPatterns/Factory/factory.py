class Dog:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """The factory method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


if __name__ == "__main__":
    dog = get_pet("dog")
    print(dog.speak())

    cat = get_pet("cat")
    print(cat.speak())

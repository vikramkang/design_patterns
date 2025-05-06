class Korean:
    """Korean Speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class English:
    """English speaker"""

    def __init__(self):
        self.name = "English"

    def speak_english(self):
        return "Hello"


class Adapter:
    """This is the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object

        # Add a new dictionary item that establishes the mapping between generic method and individualized method names
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of the attributes"""
        return getattr(self._object, attr)


if __name__ == "__main__":
    objects = []
    korean = Korean()
    english = English()
    objects.append(Adapter(korean, speak=korean.speak_korean))
    objects.append(Adapter(english, speak=english.speak_english))

    for object in objects:
        print("{} says {}".format(object.name, object.speak()))

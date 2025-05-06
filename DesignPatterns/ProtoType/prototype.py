import copy


class ProtoType:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Registers an Object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregisters object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clones a registered object and updates its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return "{}|{}|{}".format(self.name, self.color, self.options)


if __name__ == "__main__":
    c = Car()
    prototype = ProtoType()
    prototype.register_object("Skylark", c)
    c1 = prototype.clone("Skylark", color="Blue", options="UpdatedEx")
    print(c)
    print(c1)

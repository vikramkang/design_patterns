class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):  # Inherited  from abstract component class
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = args[0]

    def component_function(self):
        print("{}".format(self.name))


class Composite(Component):  # Inherited  from abstract component class
    """Concrete class and maintains tree recursive structure"""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = args[0]
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print("{}".format(self.name))
        for i in self.children:
            i.component_function()

if __name__ == "__main__":
    # Build the composite sub menu 1
    sub1 = Composite("Submenu1")
    # Create the new child sub_submenu 11
    sub11 = Child("sub_submenu 11")
    # Create the new child sub_submenu 11
    sub12 = Child("sub sub_menu 12")

    # Add children sub11 and sub12 to submenu 1
    sub1.append_child(sub11)
    sub1.append_child(sub12)

    # Build a top level component
    top = Composite("Topmenu")

    # Build a submenu2 that is ot a composite
    sub2 = Child("Submenu2")

    # Add the composite submenu 1 to the top level composite menu
    top.append_child(sub1)

    # Add the composite submenu 2 to the top level composite menu
    top.append_child(sub2)

    # Let's test
    top.component_function()


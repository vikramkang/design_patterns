class House(object):  # The class being visited
    def accept(self, visitor):
        """Interface to accept the visitor"""
        visitor.visit(self)  # Triggers the visiting operation

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)  # Note we have reference to hvac visitor object

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)  # Note we have reference to electrician visitor object

    def __str__(self):
        """Simply return the class name when the house object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract Visitor"""

    def __str__(self):
        return self.__class__.__name__


class HVACSpecialist(Visitor):
    
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)


if __name__ == "__main__":
    # Create Visitors

    hvac = HVACSpecialist()
    electrician = Electrician()

    # Create House
    house = House()

    # Visitor can be called by house
    house.accept(hvac)
    house.accept(electrician)

    # Or visitors can visit on their own
    hvac.visit(house)
    electrician.visit(house)

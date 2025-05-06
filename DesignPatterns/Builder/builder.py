class Car:
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return "{}|{}|{}".format(self.model, self.tires, self.engine)


class Builder:
    """Abstract builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

    def add_model(self):
        pass

    def add_tires(self):
        pass

    def add_engine(self):
        pass


class SkyLarkBuilder(Builder):
    """Concreate builder"""

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular Tyres"

    def add_engine(self):
        self.car.engine = "Turbo Engine"


class Director:
    """Director"""

    def __init__(self, builder: Builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


if __name__ == "__main__":
    director = Director(builder=SkyLarkBuilder())
    director.construct_car()
    car = director.get_car()
    print(car)


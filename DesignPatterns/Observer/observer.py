class Subject(object):
    def __init__(self):
        self._observers = []  # This is the list of reference of all the associated observers

    def attach(self, observer):
        # If the observer is not in the list, add it
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        # Detach the observer from the lust, if present
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:  # For all observers in the list
            if modifier != observer:  # Don't notify the observer, who is making the change
                observer.update(self)  # Alert the observers!


class Core(Subject):
    def __init__(self, name=""):
        super().__init__()
        self.name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value
        # Notify the observers when core temperature changes
        self.notify(self)

    def update(self, subject):
        print("Temperature Core: {} has temperature: {}".format(subject.name, subject.temp))


class TempViewer:
    def update(self, subject):
        print("Temperature Viewer: {} has temperature: {}".format(subject.name, subject.temp))


if __name__ == "__main__":
    # Create subjects
    c1 = Core("Core1")
    c2 = Core("Core2")

    # Create Observers
    v1 = TempViewer()
    v2 = TempViewer()

    # Attach observers
    c1.attach(v1)
    c1.attach(v2)

    # The subjects can also act as observers
    c1.attach(c1)
    c1.attach(c2)

    # Let's change the temperature of the first core
    c1.temp = 80
    c1.temp = 90



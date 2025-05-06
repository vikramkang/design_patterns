class Borg:
    """The Borg design pattern"""
    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make an attribute of dictionary


class Singleton(Borg):
    """The singleton class"""

    def __init__(self, **kwargs):
        super().__init__()
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)


if __name__ == "__main__":
    x = Singleton(HTTP="Hyper Text Transfer Protocol")
    print(x)
    y = Singleton(STP="Standard text protocol")
    print(y)

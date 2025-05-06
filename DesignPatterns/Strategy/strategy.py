import types

"""This basically replaces the function defined inside of the class by any other method declared outside of the class"""


class Strategy:
    """The strategy pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"
        # If a reference to a function is provided, replace the execution
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # This gets replaced by another version
        """The default method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))


# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


if __name__ == "__main__":
    # Let's create our default strategy
    strategies = []
    s0 = Strategy()
    # s0.execute()
    strategies.append(s0)

    # Let's create the first variation of our default strategy by providing s function argument
    s1 = Strategy(strategy_one)

    # Let's set its name
    s1.name = "Strategy one"
    strategies.append(s1)

    # Let's execute the strategy one
    # s1.execute()

    # Let's create the 2nd variation of our default strategy by providing s function argument
    s2 = Strategy(strategy_two)

    # Let's set its name
    s2.name = "Strategy two"
    strategies.append(s2)

    # Let's execute the strategy two
    # s2.execute()
    for strategy in strategies:
        strategy.execute()

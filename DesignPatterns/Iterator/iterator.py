"""Note: This can be useful when we have to iterate through numbers without worrying about getting IndexError"""


def count_to(count, numbers):
    """Iterator Implementation"""

    # Built in iterator
    # Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers)

    # Iterate through iterable list
    # Extract the German numbers
    # Put them in generator called number

    for position, number in iterator:
        # Returns a "generator" containing numbers in German
        yield number


if __name__ == "__main__":
    # list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    for num in count_to(3, numbers_in_german):
        print("{}".format(num))
    print("_" * 20)
    for num in count_to(5, numbers_in_german):
        print("{}".format(num))
    print("_" * 20)
    for num in count_to(6, numbers_in_german):
        print("{}".format(num))

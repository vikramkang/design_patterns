from functools import wraps


def make_blink(function):
    """This makes the decorator transparent in terms of name and docs, this means, when called __name__ and __doc__ of a
     function on which decorator is applied, it returns __name__ and __doc__ of original function and not of decorator"""
    @wraps(function)
    # Define the inner function
    def decorator():
        """Defines the decorator"""
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality tp the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


@make_blink
def hello_world():
    """returns Hello World."""
    return "Hello World"

@make_blink
def print_one():
    return "print 1"


print(hello_world())
print(hello_world.__name__)
print(hello_world.__doc__)

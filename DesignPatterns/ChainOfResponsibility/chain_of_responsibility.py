class Handler:  # Abstract handler
    """Abstract handler"""

    def __init__(self, successor):
        # Define who is next handler
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)  # If handled, stop here

        # Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide an implementation in the sub")


class ConcreteHandler1(Handler):
    """Concrete handler 1"""

    def _handle(self, request):
        if 0 < request <= 10:  # A condition for handling
            print("Request {} handled in handler 1".format(request))
            return True


class ConcreteHandler2(Handler):
    """Concrete handler 2"""

    def _handle(self, request):
        if 10 < request <= 20:  # A condition for handling
            print("Request {} handled in handler 2".format(request))
            return True


class ConcreteHandler3(Handler):
    """Concrete handler 3"""

    def _handle(self, request):
        if 20 < request <= 30:  # A condition for handling
            print("Request {} handled in handler 3".format(request))
            return True



class DefaultHandler(Handler):

    def _handle(self, request):
        # No condition
        print("End of chain, no handler for {}".format(request))
        return True


class Client:  # This will use handlers
    def __init__(self):
        # Create handlers and use them in the sequence you want
        self.handler = ConcreteHandler1(ConcreteHandler2(DefaultHandler(None)))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


if __name__ == "__main__":
    # Create a client
    c = Client()

    # Provide list of requests
    requests = [2, 15, 25]

    # Delegate the requests
    c.delegate(requests)

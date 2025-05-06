import time


class Producer:
    """Define the 'resource-intensive' object to instantiate!"""

    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you now")


class Proxy:
    """Define the 'relatively less resource intensive' proxy to instantiate"""

    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """Check if producer is available"""
        print("Artist checking if Producer is available")
        if self.occupied == "No":
            self.producer = Producer()
            time.sleep(2)

            # Make produce meet the guest
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy")


if __name__ == "__main__":
    p = Proxy()
    p.produce()
    
    p.occupied = "yes"
    p.produce()


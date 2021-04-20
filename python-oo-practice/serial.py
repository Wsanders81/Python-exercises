"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
#* should work using --> serial = SerialGenerator(start=100)
#TODO provide function to reset the number back to the original start number
    #* serial.reset()
#TODO put in docstrings for all methods


    def __init__(self, start): 
        """Initializes class, creates variable for start number"""
        self.start = start
        self.next = self.start

    def __repr__(self): 
        """Returns string representing SerialGenerator object"""
        return f"Serial number with start = {self.start} & next = {self.next +1}"

    def generate(self): 
        """Increments self.start and returns new serial number"""
        self.next += 1
        return self.next
    
    def reset(self): 
        self.next = self.start
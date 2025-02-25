

class calculator:
    def __init__(self, values: list) -> None:
        """Init calculator object with a vector"""
        self.values = values

    def __add__(self, object: float) -> None:
        """
        Adds a scalar to each element of the vector.
        """
        self.values = [x + object for x in self.values]
        print(self.values)

    def __mul__(self, object: float) -> None:
        """
        Multiplie chaque élément du vecteur par un scalaire.
        """
        self.values = [x * object for x in self.values]
        print(self.values)

    def __sub__(self, object: float) -> None:
        """
        Subtracts a scalar from each element of the vector.
        """
        self.values = [x - object for x in self.values]
        print(self.values)

    def __truediv__(self, object: float) -> None:
        """
        Divides each element of the vector by an object, except if the object is 0.
        """
        if object == 0:
            print("Error: Division by zero is not allowed!")
            return
        self.values = [x / object for x in self.values]
        print(self.values)

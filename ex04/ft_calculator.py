class calculator:
    """
    Class for performing calculations on vectors:
    - Dot product
    - Addition
    - Subtraction
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calcule the dot product of two vectors and displays the result.
        """
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise and displays the result.
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"add vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts two vectors element-wise and displays the result.
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"sous vector is: {result}")

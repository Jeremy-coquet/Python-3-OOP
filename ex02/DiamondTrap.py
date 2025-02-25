from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class representing Joffrey Baratheon, inheriting from both
    Baratheon and Lannister families.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes the King with the characteristics of a Baratheon,
        but with the appearance of a Lannister.
        """
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs

    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hairs = color

from S1E9 import Character


class Baratheon(Character):
    """
    Class representing a character from the Baratheon family.
    Inherits from the Character class and defines attributes
    specific to the Baratheon family.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a character from the Baratheon family with a first name,
        a life status, and specific attributes.
        :param first_name: Character's name (str)
        :param is_alive: Character's life status (bool, True by default)
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Returns a string representation for the Baratheon family.
        """
        return f"Representing the {self.family_name} family."

    def __repr__(self):
        """
        Returns a detailed string representation for the Baratheon family.
        """
        return f"Baratheon({self.first_name}, {self.eyes}, {self.hairs})"

    def die(self):
        self.is_alive = False
        return "you are died"


class Lannister(Character):
    """
    Class representing a character from the Lannister family.
    Inherits from the Character class and defines attributes
    specific to the Lannister family.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a character from the Lannister family
        with a first name, a life status, and specific attributes.
        :param first_name: Character's name (str)
        :param is_alive: Character's life status (bool, True by default)
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Returns a string representation for the Lannister family.
        """
        return f"Representing the {self.family_name} family."

    def __repr__(self):
        """
        Returns a detailed string representation for the Lannister family.
        """
        return f"Lannister({self.first_name}, {self.eyes}, {self.hairs})"

    def die(self):
        """
        Sets is_alive to False, meaning the character is dead.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Class method to create a Lannister character.
        :param first_name: Name of the character (str)
        :param is_alive: Life status (bool, True by default)
        :return: A new instance of Lannister
        """
        return cls(first_name, is_alive)

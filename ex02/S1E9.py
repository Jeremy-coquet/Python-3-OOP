from abc import ABC, abstractmethod


class Character(ABC):
    """
    abstract class character with two parameters first_name and is_alive
    """

    def __init__(self, first_name, is_alive=True):
        """
        "Initializes a character with a first name and a life status.
        :param first_name: Character's name (str)
        :param is_alive: Character's life status (bool, True by default)"
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Abstract method that must be implemented in child classes.
        It allows the character to die.
        """
        pass


class Stark(Character):
    """
    Initializes a member of the Stark family.
    Inherits from Character and implements the die() method.
    """
    def __init__(self, first_name, is_alive=True):
        """
        :param first_name: Character's name (str)
        :param is_alive: Character's life status (bool, True by default)
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Kills the character by setting is_alive to False.
        """
        self.is_alive = False

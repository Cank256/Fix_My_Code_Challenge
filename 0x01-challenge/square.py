#!/usr/bin/python3
"""
A class of a square with respective functions
"""

class Square():
    """A class representing a square.

    Attributes:
        width (int): The width of the square.
        height (int): The height of the square.
    """

    def __init__(self, width, height):
        """Initializes a new instance of the Square class.

        Args:
            width (int): The width of the square.
            height (int): The height of the square.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """Returns the perimeter of the square."""
        return (self.width + self.height) * 2

    def __str__(self):
        """Returns a string representation of the square."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())

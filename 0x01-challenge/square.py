#!/usr/bin/python3

class Square:
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

    def area(self):
        """Returns the area of the square."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the square."""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the square."""
        return f"{self.width}/{self.height}"


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())

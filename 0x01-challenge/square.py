#!/usr/bin/python3
""" A module for handling squares. """


class Square:
    """Represents a rectangle with equal sides."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a new square. """
        for key, value in kwargs.items():
            setattr(self, key, value)
            if key == 'height':
                setattr(self, 'width', value)
            if key == 'width':
                setattr(self, 'height', value)

    def area_of_my_square(self):
        """ Computes the area of this square. """
        return self.width * self.width

    def permiter_of_my_square(self):
        """ Computes the perimeter of this square. """
        return (self.width * 4)

    def __str__(self):
        """ Computes the string format of this square. """
        return "{:d}/{:d}".format(self.width, self.width)


if __name__ == "__main__":
    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

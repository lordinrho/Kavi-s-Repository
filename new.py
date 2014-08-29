__author__ = 'lord'
from numbers import Number
import numpy
def square_perimeter(side : Number) -> Number:
    """
    Calculate perimeter of a square from side length.
    @param side: the side length
    @return: the perimeter (same units as side length)
    >>> square_perimeter(4)
    16
    """
    return 4*side


def square_area(side):
    """
    Calculate area of a square from side length.
    :param side: the side length
    :return: the area (units^2 from side)
    >>> square_area(4)
    16
    """
    return side*side

if __name__ == "__main__":
    sampleSide = 4
    print("area:",
          square_area(sampleSide),
          "perimeter:",
          square_perimeter(sampleSide))

def pyramid_volume(base_area, height):
    """
    Calculates the volume of a pyramid
    :param base_area: the area of the base of the pyramid
    :param height: the altitude of the pyramid
    :return: the volume
    >>>pyramid_volume(9,5)
    15
    """
    volume = 1/3*base_area*height
    return volume
if __name__ == "__main__":
    base_area = 9
    height = 5
    print("The Volume of the Pyramid is",
          pyramid_volume(base_area, height))


def sphere_area(radius):
    """
    Calculating the surface area of a sphere
    :param radius: radius of the sphere
    :return: the surface area
    >>>sphere_area(4)
    201.06192983
    """
    area = 4*numpy.pi*radius**2
    return area

if __name__ == "__main__":
    radius = 4
    print("The Surface Area of the Sphere is",
          sphere_area(4))


def sphere_volume(radius):
    """
    Calculating the volume of a sphere
    :param radius: radius of the sphere
    :return: the volume
    >>>sphere_area(3)
    113.097335529
    """
    volume = 4/3*numpy.pi*radius**3
    return volume
if __name__ == "__main__":
    radius = 3
    print("The Volume of the Sphere is",
          sphere_volume(radius))
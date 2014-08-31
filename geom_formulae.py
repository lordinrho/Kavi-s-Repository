__author__ = 'lord'
import numpy


def rectangle_area(width, length):
    """
    Calculating the area of a rectangle
    :param width: width side of rectangle
    :param length: length side of rectangle
    :return: rectangle_area (unit of width * unit of length)
    >>> rectangle_area(4,5)
    20
    """
    return width*length

if __name__ == "__main__":
    samplewidth = 4
    samplelength = 5
    print("The area of the Rectangle is",
         rectangle_area(samplewidth, samplelength))


def rhombus_area(diagonal1, diagonal2):
    """
    calculating the area of a rhombus using its two diagonal lengths
    :param diagonal1: length of first diagonal
    :param diagonal2: length of other diagonal
    :return: rhombus_area
    >>>rhombus_area(3,4)
    12
    """
    return diagonal1*diagonal2

if __name__ == "__main__":
    diagonal1 = 3
    diagonal2 = 4
    print("The Area of the Rhombus is",
          rhombus_area(diagonal1, diagonal2))


def trapezoid_area(base1, base2, height):
    """
    Calculating the area of a Trapezoid
    :param base1: the length of the first base
    :param base2: the length of the other base
    :param height: the altitude
    :return: Trapezoid_area
    >>>trapezoid_area(5,3,4)
    16
    """
    return 0.5*height*(base1+base2)

if __name__ == "__main__":
    base1 = 5
    base2 = 3
    height = 4
    print("The Area of the Trapezoid is",
          trapezoid_area(base1, base2, height))


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
    >>>sphere_volume(3)
    113.097335529
    """
    volume = 4/3*numpy.pi*radius**3
    return volume

if __name__ == "__main__":
    radius = 3
    print("The Volume of the Sphere is",
    sphere_volume(radius))


def circle_area(radius=None, diameter=None):
    """
    Calc
    :param radius: radius
    :param diameter: dia
    :return: area
    """

    if radius is None:
        area1 = 1/4*numpy.pi*diameter**2
        return area1
    else:
        area2 = numpy.pi*radius**2
        return area2
print("Area of circle using radius is", circle_area(radius = 4))
print("Area of circle using diameter is", circle_area(diameter = 8))


def cylinder_area(radius, height):
    """
    Calculating the area of a cylinder
    :param radius: the radius of the cylinder
    :param height: the height of the cylinder
    :return: the area
    >>>cylinder_area(3,5)
    94.247779608
    """
    area = 2*numpy.pi*radius*height
    return area


def cylinder_volume(radius, height):
    """
    Calculating the volume of a cylinder
    :param radius: the radius of the cylinder
    :param height: the height of the cylinder
    :return: the volume
    >>>cylinder_volume(3,5)
    141.371669412
    """
    volume = numpy.pi*(radius**2)*height
    return volume

if __name__ == "__main__":
    print("The area of the cylinder is",
          cylinder_area(3, 5), "\n"
          "The volume of the cylinder is",
          cylinder_volume(3, 5))


def cone_volume(radius, height):
    """
    Calculating the volume of a cone
    :param radius: the radius of the cone
    :param height: the height of the cone
    :return:volume
    >>>cone_volume(3,5)
    47.123889804
    """
    volume = (1/3)*numpy.pi*(radius**2)*height
    return volume


def cone_area(radius, height):
    """
    Calculating the area of a cone
    :param radius: the radius of the cone
    :param height: the height of the cone
    :return: the area
    >>>cone_area(3,5)
    54.955426909
    """
    area = numpy.pi*radius*((radius**2+height**2)**(1/2))
    return area

if __name__ == "__main__":
    print("The volume of the cone is",
          cone_volume(3, 5), "\n"
          "The area of the cone is",
          cone_area(3, 5))
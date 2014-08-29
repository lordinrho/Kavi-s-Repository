__author__ = 'lord'
import numpy


def circle_area1(radius):
    """
    calculating the surface area of a circle using its radius
    :param radius: the radius of the circle
    :return: Circle_area
    >>>circle_area1(3)
    28.274333
    """
    area1 = numpy.pi*radius**2
    #area2 = 1/4*numpy.pi*diameter**2
    return area1
if __name__ == "__main__":
    radius = 3
    print("The area of the circe using its radius is",
          circle_area1(radius))

def circle_area2(diameter):
    """
    Calculating the surface area of a circle using its diameter
    :param diameter: the diameter of the circle
    :return: the surface area
    >>>circle_area2(6)
    28.274333
    """
    area2 = 1/4*numpy.pi*diameter**2
    return area2
if __name__ == "__main__":
    print("The area of the circle using its diameter is",
          circle_area2(6))


#AN ALTERNATE WAY OF SOLVING THE ABOVE
def circle_area(radius = None, diameter = None):
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

print("area using radius is", circle_area(radius = 4))
print("area using diamter is", circle_area(diameter = 8))



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
    volume = numpy.pi*(radius**2)*(height)
    return volume
if __name__ == "__main__":
    print("The area of the cylinder is",
          cylinder_area(3, 5),
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
    area = (numpy.pi)*radius*((radius**2+height**2)**(1/2))
    return area

if __name__ == "__main__":
    print("The volume of the cone is",
          cone_volume(3, 5),
          "The area of the cone is",
          cone_area(3, 5))
__author__ = 'lord'
def triangle_area(base, height):
    """
    calculates area of triangle
    :param base: base length
    :param height: length of height
    :return: the area of the triangle (square unit of base)
    >>>triangle_area(4,8)
    16
    """
    return base*height/2

if __name__ =="__main__":
    print("the area of the triangle is",
    triangle_area(4, 6))

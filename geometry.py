import math
def triangle_area(b, h):
    a = (1/2) * b * h
    return a
def circle_area(r):
    a = math.pi * r**2
    return a
def parallelogram_area(b, h):
    a = b * h
    return a
def trapezoid_area(A, b, h):
    a = ( (A + b) / 2) * h
    return a
def rectangular_prism_volume(w, h, l):
    v = w * h * l
    return v
def cone_volume(r, h):
    v = math.pi * r**2 * (h / 3)
    return v
def sphere_volume(r):
    v = (4 / 3) * math.pi * r**3
    return v
def rectangular_prism_surface_area(w, l, h):
    a = 2 * ((w * l) + (h * l) + (h * w))
    return a
def sphere_surface_area(r):
    a = 4 * math.pi * r**2
    return a
def hypotenuse(a, b):
    c = (a**2 + b**2)**(1 / 2)
    return c
def herons_formula(a, b, c):
    s = (a + b + c) / 2
    return s








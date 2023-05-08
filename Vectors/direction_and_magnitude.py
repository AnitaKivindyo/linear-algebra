from arithmetics import Vector

'''Magnitude and direction In Vectors
Magnitude
In vectors , Magnitude refers to the length or size of a vector. i.e : the distance from the origin of the vector space to the tip of the vector.
The magnitude of the vector is denoted as ||v||, where v is the vector.
Formular of calculating the magnitude of a vector is:

||v|| = sqrt(v1**2 + v2**2 + v3**2 + v4**2...+vn**2), wher v1,v2...,vn are the components of the vector.

Direction
Direction is a vector is represented by a unit vector. Normalization is the process of finding a unit vector.
Normalization involves scaling the vector to become 1. This is done by dividing each component of the vector by the magnitude of the vector.

v_norm = v / ||v||

The resulting vector v_norm is called normalized vector. 
Normalizing is useful for many purpose, such as finding the direction of a vector, comparing vectors, and simplifying calculations involving vectors
'''

class Mag_and_D(Vector):
    ''' Magnitude and Normalization class 

    Attributes:
        object
    '''

    def __init__(self):

        Vector.__init__(self)

    def claculate_magnitude(self):
        None

    def calculate_normalization(self):
        None


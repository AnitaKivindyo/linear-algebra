class Vector(object):
    def __init__(self, coordinates):
        ''' This initializer creates a vector based on the input list of coordinates
           and also sets the dimesnion of space the vector lives in
        '''      
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        
        except ValueError:
            raise ValueError('The coordinates must be an iterable')
        
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
    
    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def __add__(self, other):
        if self.dimension != other.dimension:
            raise ValueError('The dimension of the 2 vectors should be the same')
        new_coordinates= [x+y for x,y in zip(self.coordinates,other.coordinates)]
        return 'added vector: {}' .format (Vector([round(x,3) for x in new_coordinates]))
        
    def __sub__(self, other):
        if self.dimension != other.dimension:
            raise ValueError('The dimension of the 2 vectors should be the same')
        new_coordinates = [x-y for x,y in zip(self.coordinates,other.coordinates)]
        return 'minus vector: {}'.format(Vector([round(x,3) for x in new_coordinates]))
        
    def __mul__(self, scalar):
        new_coordinates = [scalar*x for x in self.coordinates]
        return 'multiplied vector: {}'.format(Vector([round(x,3)for x in new_coordinates]))


my_vector = Vector([1,2,3])
print (my_vector)

vector2 = Vector([5,6,9,8])
vector3 =Vector([1,2,3])

print (vector2 == my_vector)
print (vector3 == my_vector)
print (vector3 == vector2)

v1 = Vector([8.218,-9.341])
v2 = Vector([-1.129,2.111])
v3 = v1 + v2
print(v3)
v4 = Vector([7.119,8.215])
v5= Vector([-8.223,0.878])
v6 = v4 - v5
print(v6)
v7 = Vector([1.671,-1.012,-0.318])
v8 = v7 * 7.41
print(v8)

import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.magnitude = self.calculateMagnitude()
            self.direction = self.calculateDirection()

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        list = []
        for i in range(self.dimension):
            list.append(self.coordinates[i] + v.coordinates[i])
        return Vector(list)

    def __sub__(self, v):
        list = []
        for i in range(self.dimension):
            list.append(self.coordinates[i] - v.coordinates[i])
        return Vector(list)

    def __mul__(self, v):
        list = []
        for i in range(self.dimension):
            list.append(self.coordinates[i] * v)
        return Vector(list)

    def __rmul__(self, v):
        list = []
        for i in range(self.dimension):
            list.append(self.coordinates[i] * v)
        return Vector(list)

    def __truediv__(self, v):
        list = []
        for i in range(self.dimension):
            if v == 0:
                list.append(0)
            else:
                list.append(self.coordinates[i] / v)
        return Vector(list)

    def __rtruediv__(self, v):
        list = []
        for i in range(self.dimension):
            if v.coordinates[i] == 0:
                list.append(0)
            else:
                list.append(v / self.coordinates[i])
        return Vector(list)

    def __div__(self, v):
        list = []
        for i in range(self.dimension):
            if v == 0:
                list.append(0)
            else:
                list.append(self.coordinates[i] / v)
        return Vector(list)

    def __rdiv__(self, v):
        list = []
        for i in range(self.dimension):
            if self.coordinates[i] == 0:
                list.append(0)
            else:
                list.append(v / self.coordinates[i])
        return Vector(list)

    def calculateMagnitude(self):
        squareTotal = 0.0
        for i in range(self.dimension):
            squareTotal += (self.coordinates[i] ** 2)
        result = math.sqrt(squareTotal)
        return result

    def calculateDirection(self):
        list = []
        try:
            for i in range(self.dimension):
                list.append(self.coordinates[i] / self.magnitude)
        except ZeroDivisionError as e:
            raise Exception('Cannot normalize the zero vector')
        return tuple(list)

    def magnitude(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError as e:
            raise Exception('Cannot normalize the zero vector')

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

#exercise 8

# exercise 6
# v61 = Vector([-0.221, 7.437])
# v62 = Vector([8.813, -1.331, -6.247])
# v63 = Vector([5.581, -2.136])
# v64 = Vector([1.996, 3.108, -4.554])
#
# print v61.magnitude
# print v62.magnitude
# print v63.direction
# print v64.direction

#exercise 4
# v11 = Vector([8.218, -9.341])
# v12 = Vector([-1.129, 2.111])
#
# v21 = Vector([7.119, 8.215])
# v22 = Vector([-8.223, 0.878])
#
# v31 = Vector([1.671, -1.012, -0.318])
#
# print v11+v12
# print v21-v22
# print 7.41*v31
# print 2/v11

# v1 = Vector([1,2,3])
# v2 = Vector([3,5,3])
# v3 = Vector([-2,-3,0])
# v4 = Vector([-23,4,23])
# v5 = v2+v3
# v6 = v2-v4
# v7 = v4/4
# v8 = v3*5
# v9 = v3/0
# v10 = v1*0
#
# print v1
# print v2
# print v3
# print v4
# print v5
# print v6
# print v7
# print v8
# print v9
# print v10
#
# print v1==v5
# print v1==v6
# print v2==v6
# print v6==v4

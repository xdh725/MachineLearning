import math
from decimal import Decimal, getcontext

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.magnitude = self.calculateMagnitude()
            self.direction = self.calculateDirection()

            # print "magnitude: " ,self.magnitude
            # print "direction: " ,self.direction
        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, v):
        new_coordinates = [v*x for x in self.coordinates]
        return Vector(new_coordinates)


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

    def magnitudeMethod(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitudeMethod()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError as e:
            raise Exception('Cannot normalize the zero vector')

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def convolution(self, v):
        coordinates_multiply = [x*y for x,y in zip(self.coordinates, v.coordinates)]
        return sum(coordinates_multiply)

    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    # v*w = v*w / (||v||*||w||)
    def angle_with(self, v, in_degrees=False):
        tmp_convolution = self.convolution(v)
        # print "tmp_convolution ", tmp_convolution
        # print "self.magnitude: ", self.magnitude, "v.magnitude", v.magnitude

        if self.magnitude==0 or v.magnitude==0 :
            return 0
        result = math.acos(tmp_convolution / (self.magnitude * v.magnitude))
        if in_degrees:
            return math.degrees(result)
        else:
            return result

    def isParallel(self, v):
        isParallel = False
        c1 = self.coordinates[0]
        c2 = v.coordinates[0]
        if c1==0 or c2==0:
            firstRate = 0
        else:
            firstRate = abs(Decimal(c1)/Decimal(c2))
        for i in range(1,self.dimension):
            coord1 = self.coordinates[i]
            coord2 = v.coordinates[i]
            if coord1==0 or coord2==0:
                secondRate = 0
            else:
                secondRate = abs(Decimal(coord1)/Decimal(coord2))
            if firstRate==secondRate:
                isParallel = True
            else:
                isParallel = False
                break
        print "firstRate:",firstRate
        print "secondRate:",secondRate
        return isParallel

    def isOrthogonal(self, v):
        print "convolution: ", self.convolution(v)
        if self.convolution(v)==0:
            return True
        else:
            return False

    def is_parallel_to(self, v):
        return (self.is_zero() or v.is_zero() or
                self.angle_with(v) == 0 or self.angle_with(v) == math.pi)

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.convolution(v)) < tolerance

    def is_zero(self, tolerance=1e-10):
        return (self.magnitude < tolerance)

    # v projective = v * b's normalize
    def component_parallel_to(self, basis):
        # try:
            u = basis.normalized()
            weight = self.convolution(u)
            return weight*u
        # except Exception as e:
            # if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
            # raise e
    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return (self - projection)
        except Exception as e:
            raise e

    def vectorProductIn3D(self, v):
        x1 = self.coordinates[0]
        y1 = self.coordinates[1]
        z1 = self.coordinates[2]
        x2 = v.coordinates[0]
        y2 = v.coordinates[1]
        z2 = v.coordinates[2]

        array = []
        array.append(y1*z2 - y2*z1)
        array.append(-(x1*z2 - x2*z1))
        array.append(x1*y2 - x2*y1)
        return Vector(array)

    def areaOfParallelogram(self, v):
        vectorOfProduct = self.vectorProductIn3D(v)
        return vectorOfProduct.magnitudeMethod()

    def areaOfTriangle(self, v):
        return (self.areaOfParallelogram(v) / 2.0)

# exercise 14
# v1401 = Vector([8.462, 7.893, -8.187])
# w1401 = Vector([6.984, -5.975, 4.778])
#
# v1402 = Vector([-8.987, -9.838, 5.031])
# w1402 = Vector([-4.268, -1.861, -8.866])
#
# v1403 = Vector([1.5, 9.547, 3.691])
# w1403 = Vector([-6.007, 0.124, 5.772])
#
# print v1401.vectorProductIn3D(w1401)
# print v1402.areaOfParallelogram(w1402)
# print v1403.areaOfTriangle(w1403)

# exercise 12
# v1201 = Vector([3.039, 1.879])
# w1201 = Vector([0.825, 2.036])
#
# v1202 = Vector([-9.88, -3.264, -8.159])
# w1202 = Vector([-2.155, -9.353, -9.473])
#
# v1203 = Vector([3.009, -6.172, 3.692, -2.51])
# w1203 = Vector([6.404, -9.144, 2.759, 8.718])
#
# print v1201.component_parallel_to(w1201)
# print v1202.component_orthogonal_to(w1202)
# print v1203.component_parallel_to(w1203)
# print v1203.component_orthogonal_to(w1203)

# # exercise 10
# v101 = Vector([-7.579, -7.88])
# w101 = Vector([22.737, 23.64])
#
# v102 = Vector([-2.029, 9.97, 4.172])
# w102 = Vector([-9.231, -6.639, -7.245])
#
# v103 = Vector([-2.328, -7.284, -1.214])
# w103 = Vector([-1.821, 1.072, -2.94])
#
# # test code
# v101 = Vector([2.423, 1.332])
# w101 = Vector([2.423*2, 1.332*2])
#
# v102 = Vector([-23.423, 32.222])
# w102 = Vector([23.423*2, 32.222*2])
#
# print v101.is_parallel_to(w101)
# print v102.is_parallel_to(w102)
# print v103.is_parallel_to(w103)
# print v101.is_orthogonal_to(w101)
# print v102.is_orthogonal_to(w102)
# print v103.is_orthogonal_to(w103)

#exercise 8
# v81 = Vector([7.887, 4.138])
# w81 = Vector([-8.802, 6.776])
#
# v82 = Vector([-5.955, -4.904, -1.874])
# w82 = Vector([-4.496, -8.755, 7.103])
#
# v83 = Vector([3.183, -7.627])
# w83 = Vector([-2.668, 5.319])
#
# v84 = Vector([7.35, 0.221, 5.188])
# w84 = Vector([2.751, 8.259, 3.985])
#
# print v81.convolution(w81)
# print v82.convolution(w82)
# print v83.angle(w83)
# print v84.angle(w84,True)

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

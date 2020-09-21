from fractions import Fraction 
import math
m = int(input())
tan = list(map(Fraction, input().split()))
coordinates = [] 
for i in range(m):
    x,y = (input().split())
    temp = x + '/' + y
    coordinates.append(Fraction(temp))
coordinates.sort()
print(tan)
print('tan nguyen', tan[0])
print('tan dao', 1/tan[0])
print(temp)
print(coordinates)
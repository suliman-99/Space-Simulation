from pygame import Vector3
from Other_Projects.Physics.vector import Vector

v1 = Vector3(1, 2, 3)
v2 = Vector3(4, 5, 6)

v3 = Vector(2, 0, 0)
v4 = Vector(4, 4, 4)


test = Vector(3, 2, 235)

temp = v3*(v3.dot(v4)/v3.length()**2)
temp1 = v3.dot(v4)/v3.length()
print(temp)
print(temp1)
print(v4.projection_on(v3))
print(v4.projection_length_on(v3))

# u1 = (v3*(v3.dot(test)/v3.length()**2))
# u2 = test - u1
# print(test)
# print(u1)
# print(u2)
# print(u1+u2)


# from vpython import *


# def fuzzy_puzz(num: int):
#     if num % 3 == 0 and num % 5 == 0:
#         return "fuzzy_puzz"
#     if num % 3 == 0:
#         return "fuzzy"
#     if num % 5 == 0:
#         return "puzz"
#     return num


# print(fuzzy_puzz(1))
# print(fuzzy_puzz(2))
# print(fuzzy_puzz(3))
# print(fuzzy_puzz(6))
# print(fuzzy_puzz(5))
# print(fuzzy_puzz(10))
# print(fuzzy_puzz(15))
# print(fuzzy_puzz(30))
# print(fuzzy_puzz("sss"))

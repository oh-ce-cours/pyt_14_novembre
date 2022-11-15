# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 09:42:39 2022

@author: 33612
"""

nombres_1_a_100 = range(1, 101)
# for nombre in nombres_1_a_100:
#     if nombre % 3 == 0 and nombre % 5 == 0:
#         print("FizzBuzz")
#     elif nombre % 3 == 0:
#         print("Fizz")
#     elif nombre % 5 == 0:
#         print("Buzz")
#     else:
#         print(nombre)

# for nombre in nombres_1_a_100:
#     match (nombre % 3, nombre % 5):
#         case 0, 0:
#             print("Fizzbuzz")
#         case _, 0:
#             print("Buzz")
#         case 0, _:
#             print("Fizz")
#         case _, _:
#             print(nombre)

# for nombre in nombres_1_a_100:
#     res = ""
#     if nombre % 3 == 0:
#         res = res + "fizz"
#     if nombre % 5 == 0:
#         res += "buzz"
#     if not res:
#         res = nombre
#     print(res)

for nombre in nombres_1_a_100:
    res = "fizz" * (nombre % 3 == 0) + "buzz" * (nombre % 5 == 0) or nombre
    print(res)


def regle_fizzbuzz(nombre: int) -> str:
    res = ""
    if nombre % 3 == 0:
        res = res + "fizz"
    if nombre % 5 == 0:
        res += "buzz"
    if not res:
        res = nombre

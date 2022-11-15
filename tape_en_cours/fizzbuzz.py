# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 09:42:39 2022

@author: 33612
"""

nombres_1_a_100 = range(1, 101)
for nombre in nombres_1_a_100:
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    elif nombre % 3 == 0:
        print("Fizz")
    elif nombre % 5 == 0:
        print("Buzz")
    else:
        print(nombre)

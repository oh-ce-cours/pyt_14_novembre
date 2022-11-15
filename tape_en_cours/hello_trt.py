# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math
from math import pi
from math import pi as _3_14

from math import exp
from cmath import exp as cexp


print(math.cos(pi))
print(exp(2) * cexp(3))


print("Salut TRT")
for i in range(1):
    a = 2
    if a == 3:
        print(a)
        print("yo les gens")


mes_nombres = [10, -2, 3.56] * 3  # on allonge la liste
cos_mes_nombres = []
for nombre in mes_nombres:
    cos_mes_nombres.append(math.cos(nombre))

print(len(mes_nombres))
mes_nombres_numpy = np.array(mes_nombres)
print(np.cos(mes_nombres_numpy))

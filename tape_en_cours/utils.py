# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:18:39 2022

@author: 33612
"""


def est_divisible(numerateur, denominateur) -> bool:
    return numerateur % denominateur == 0


def regle_fizzbuzz(nombre: int) -> str:
    res = ""
    if est_divisible(nombre, 3):
        res = res + "fizz"
    if est_divisible(nombre, 5):
        res += "buzz"
    if not res:
        res = nombre
    return res

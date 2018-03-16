#!/usr/bin/env python3
"""
clothing.py
Program that stores information on shirts
@author Dexter Renick
@version 2018-12-2
"""
from clothing import *

class Shirt(Clothing):
    def __init__(self, name, color, clean, material, sleeves):
        super().__init__(name, color, clean)
        self.material = material
        self.sleeves = sleeves

    def getMaterial(self):
        return self.material

    def getSleeves(self):
        return self.sleeves

    def __str__(self):
        return (super().__str__() + ", material=" + self.material + ", sleeves=" + self.sleeves + "]")

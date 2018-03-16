#!/usr/bin/env python3
"""
clothing.py
Program that stores information on pants
@author Dexter Renick
@version 2018-12-2
"""
from clothing import *

class Pants(Clothing):
    def __init__(self, name, color, clean, style, size, brand):
        super().__init__(name, color, clean)
        self.style = style
        self.size = size
        self.brand = brand

    def getStyle(self):
        return self.style()

    def getSize(self):
        return self.size()

    def getBrand(self):
        return self.brand()

    def __str__(self):
        return (super().__str__() + ", style=" + self.style + ", size=" + str(self.clean) + ", brand=" + self.brand + "]")

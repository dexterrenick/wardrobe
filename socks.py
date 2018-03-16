#!/usr/bin/env python3
"""
clothing.py
Program that stores information on socks
@author Dexter Renick
@version 2018-12-2
"""
from clothing import *

class Socks(Clothing):
    def __init__(self, name, color, clean, pattern, number):
        super().__init__(name, color, clean)
        self.pattern = pattern
        self.number = number

    def getPattern(self):
        return self.pattern()

    def getNum(self):
        return self.number()

    def __str__(self):
        return (super().__str__() + ", Pattern=" + self.pattern + ", Number=" + (str(self.number)) + "]")

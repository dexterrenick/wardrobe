#!/usr/bin/env python3
"""
wardrobe.py
Class that sorts a collection of Clothing objects into different catagories
@author Dexter Renick
@version 2018-12-2
"""
from clothing import *
from pants import *
from socks import *
from shirt import *

class Wardrobe():
    def __init__(self, myClothes):
        self.clothes = myClothes

    def addClothes(self, article):
        self.clothes.append(article)

    def removeClothes(self, article):
        self.clothes.remove(article)

    def showClothes(self):
        allClothes=[]
        for i in range(len(self.clothes)):
            allClothes.append(str(self.clothes[i]))
        return allClothes

    def showPants(self):
        allPants=[]
        for i in range(len(self.clothes)):
            if isinstance(self.clothes[i], Pants):
                allPants.append(str(self.clothes[i]))
        return(allPants)

    def showShirts(self):
        allShirts=[]
        for i in range(len(self.clothes)):
            if isinstance(self.clothes[i], Shirt):
                allShirts.append(str(self.clothes[i]))
        return(allShirts)

    def showSocks(self):
        allSocks=[]
        for i in range(len(self.clothes)):
            if isinstance(self.clothes[i], Socks):
                allSocks.append(str(self.clothes[i]))
        return(allSocks)

    def showClean(self):
        cleanclothes = []
        for i in range(len(self.clothes)):
            if self.clothes[i].isClean():
                cleanclothes.append(str(self.clothes[i]))
        return cleanclothes

    def showDirty(self):
        dirtyclothes = []
        for i in range(len(self.clothes)):
            if not self.clothes[i].isClean():
                dirtyclothes.append(str(self.clothes[i]))
        return dirtyclothes

    def showColor(self, color):
        clothescolor = []
        for i in range(len(self.clothes)):
            if self.clothes[i].getColor() == color:
                clothescolor.append(str(self.clothes[i]))
        return clothescolor

    def findClothingBySleeveLength(self, sleeves):
        sleevedclothes = []
        for i in range(len(self.clothes)):
            if isinstance(self.clothes[i], Shirt):
                if self.clothes[i].getSleeves() == sleeves:
                    sleevedclothes.append(str(self.clothes[i]))
        return sleevedclothes

    def washClothes(self):
        cleanClothes = []
        for i in range(len(self.clothes)):
            self.clothes[i].setClean(True)
            cleanClothes.append(str(self.clothes[i]))
        return cleanClothes



if __name__ == "__main__":
    main()

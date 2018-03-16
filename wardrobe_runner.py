#!/usr/bin/env python3
"""
wardrobe_runner.py
Program that manages a collection of Clothing objects
@author Dexter Renick
@version 2018-12-2
"""
from clothing import *
from pants import *
from socks import *
from shirt import *
from wardrobe import *
import time

def main():
    clothingArticles = [(Shirt("Favorite Shirt", "Red", True, "Cotton", "Short")),(Shirt("Concert Tee", "Graphic Tee", True, "Denim", "Long")),(Shirt("Striped Tee", "Black and White Stripes", False, "Polyester Mix", "Short")),(Pants("Acid-Washed Jeans", "Light-Blue", False, "Chino", "30x32", "Levi's")),(Pants("Favorite Pants", "Tartan Print", True, "Chino", "32x34", "G-Star by Elwood")), (Pants("Every-day Pants", "Black", False, "Corduroy", "Small", "A.P.C.")),(Socks("Favorite Socks", "blue", False, "striped", 3)), (Socks("Formal Socks", "Black", True, "Solid Color", 4))]
    wardrobe = Wardrobe(clothingArticles)

    "Show your Clothing items"
    print("\n==== Full Wardrobe ====")
    allClothes = wardrobe.showClothes()
    print (allClothes)
    print()

    "Adds Article of clothing"
    print("*Adding your Casual Socks to the wardrobe*")
    print()
    wardrobe.addClothes((Socks("Casual Socks", "Pink and White", True, "Polka-Dot", 2)))

    "Show your socks"
    print("\n==== All Socks ====")
    allSocks = wardrobe.showSocks()
    print(allSocks)
    print()

    "Show your shirts"
    print("\n==== All Shirts ====")
    allShirts = wardrobe.showShirts()
    print(allShirts)
    print()

    "Show your pants"
    print("\n==== All Pants ====")
    allPants = wardrobe.showPants()
    print(allPants)
    print()

    "Show your dirty clothes"
    print("\n==== Dirty Clothes ====")
    mydirtyclothes = wardrobe.showDirty()
    print(mydirtyclothes)
    print()

    "Show your clean clothes"
    print("\n==== Clean Clothes ====")
    mycleanclothes = wardrobe.showClean()
    print(mycleanclothes)
    print()

    "Show your Black clothes"
    print("\n==== Black Clothes ====")
    blackclothes = wardrobe.showColor("Black")
    print(blackclothes)
    print()

    "Show Sleeved Shirts"
    print("\n==== Sleeved Clothes ====")
    sleevedclothes = wardrobe.findClothingBySleeveLength("Short")
    print(sleevedclothes)
    print()

    print("*Washing Clothes*")
    print()

    print("Your clothes are now clean!")

    "Show Clean Shirts"
    print("\n==== Cleaned Clothes (All Clothes) ====")
    cleanclothes = wardrobe.washClothes()
    print (cleanclothes)






if __name__ == "__main__":
    main()

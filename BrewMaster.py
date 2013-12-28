#BREWMASTER
#A game by Isaac Smith
#Coded in Python 2.7 (32-Bit) with the pyGame module
#Contact at isaac4266@gmail.com

#TODO: new HopsHelping class means that the hops attribute for Recipes
#is now a multi-item list. Adding to recipe in-game must reflect this.
#Perhaps it's time for a GUI... blargh...
#Since one while loop won't work (especially with added grains/extras),
#It would be best to put each ingredient addition in an individual method
#and store those methods in another class, perhaps "brewing.py"

#TODO: Brewing successfully produces an instance of the "Beer" class.
#This means implementing parts of the Brewery class (mainly storage)

import random, time, sys, pygame
import recipes
import ingredients
from pygame.locals import *

NUMBERS_0_TO_9 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
class Brewery:
    def __init__(self, kettles, max_storage, inventory = Inventory()):
        self.kettles = kettles
        self.max_storage = max_storage
        self.ledger = []
        self.storage = 0
        self.inventory = inventory

class Beer:
    def __init__(self, ingredients, volume):
        self.ingredients = ingredients
        self.volume = volume
        self.age = 0
        self.bottled = False
        self.bottle = None
        self.name = None
        self.quality = 10

    def bottle(self, bottle_type):
        self.bottle = bottle_type
        self.bottled = True

class Inventory:
    def __init__(self):
        self.barrels = []
        self.cases = []
        self.ingredients = []


    


def check_if_num(input_string):
    input_list = list(input_string)
    if len(input_list) > 0:
        for i in range(len(input_list)):
            if input_list[i] not in NUMBERS_0_TO_9:
                return False
        return True





brewery = Brewery(2, 100)
print "It is the year 2025..."
print "In Germany, a bitter war has been waged"
print "between the brewmasters of the largest"
print "breweries. During the war, Germany was"
print "reduced to many feuding city-states,"
print "each favoring their own brewmaster and"
print "their local beer."
print " "
#time.sleep(5)
print "The war ended in a vicious double-coup"
print "that destroyed the last two powerful"
print "German breweries. The hope for German"
print "beer seemed dim. In a last-ditch effort,"
print "the German High Council suspended the"
print "Deutsches Reinheitsgebot (the beer"
print "purity law), to inspire new brewers to"
print "come together and revitalize Germany's"
print "beer industry."
print " "
#time.sleep(7)
print "You are one such new brewer. Can you reunite"
print "Germany? You must become the new world's first..."
#time.sleep(2.5)
print "."
#time.sleep(0.5)
print "."
#time.sleep(0.5)
print "."
#time.sleep(0.5)
print "BREWMASTER!"

time.sleep(1)
is_playing = True
while is_playing:
    print "It's brewing time!"
    print "What is your beer's name?"
    name = raw_input()
    brewing = recipes.Recipe(name)
    ingredient_names = [brewing.malt_type.name, brewing.bitters_type.name,
                        brewing.hops_type.name, "yeast"]
    ingredient_types = ['syrup', 'bitters', 'hops', '']
    ingredient_amounts = [brewing.malt_syrup, brewing.bitters, brewing.hops,
                        brewing.yeast]
    for i in range(4):
        print ("How much " + ingredient_names[i] +
               " " + ingredient_types[i] + " do you want to use?")
        while True:
            amount = raw_input()
            if not check_if_num(amount):
                print "Please enter a number. (0 is acceptable)"
            else:
                ingredient_amounts[i] = int(amount)
                break
    brewing.malt_syrup = ingredient_amounts[0]
    brewing.bitters = ingredient_amounts[1]
    brewing.hops = ingredient_amounts[2]
    brewing.yeast = ingredient_amounts[3]
    

    print "Your beer has been brewed!"
    time.sleep(1)
    for i in range(3):
        print "Analyzing..."
        time.sleep(1)
    brewed_something = False
    for recipe in recipes.recipes:
        if recipe.brewed_me(brewing):
            brewed_something = True
            print ("You brewed " + brewing.name + ", a "
                   + recipe.name +
                   "! Congratulations!")

    if not brewed_something:
        print "Your beer didn't turn out right (or perhaps"
        print "the world just isn't ready for it yet)!"
    print "Brew again? Y/N"
    decision = raw_input()
    if list(decision)[0].lower() != 'y':
        is_playing = False
        print "Thanks for playing!"
        break



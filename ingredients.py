#Ingredients file for BREWMASTER

class Grain:
    def __init__(self, name, grain_type = "Syrup Extract"):
        self.name = name
        self.type = grain_type

class Hops:
    def __init__(self, name, aa = 12):
        self.name = name
        self.aa = aa

class HopsHelping:
    def __init__(self, hops, amount, time):
        self.hops = hops
        self.amount = amount
        self.time = time
        #alpha acid units: a measurement of bitterness/flavor
        #used to determine if a recipe has been made
        self.aau = hops.aa * amount * 0.1
    def get_attributes(self):
        return (self.aau, self.time)

Pale = Grain("Pale")
Wheat = Grain("Wheat", "Grain")
Nugget =  Hops("Nugget")
Cascade = Hops("Cascade", 5)

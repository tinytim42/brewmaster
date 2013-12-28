#Recipes file for BREWMASTER
#Contains recipe class, and all recipes
#All recipes are for a 5-gallon yield
import ingredients

class Recipe:
    #Initializes recipe to Cincinnati Pale Ale
    #Hops amount is in tenths of an ounce. 10 = 1 oz.
    def __init__(self, name, grain_type = ingredients.Pale,
                 grain_amount = 4,
                 hops_helpings =
                 [ingredients.HopsHelping(ingredients.Nugget, 10, 0),
                  ingredients.HopsHelping(ingredients.Cascade, 10, 45)],
                 yeast = 2, extras = [], boil_time = 60,
                 temp_range = (65, 70)):
        self.name = name
        self.grain_type = grain_type
        self.grain_amount = grain_amount
        self.hops_helpings = hops_helpings
        self.yeast = yeast
        self.extras = extras
        self.boil_time = boil_time
        self.temp_range = temp_range

    #adds hops to the recipe, takes an argument "hops"
    #"hops" is a 3-item list: a Hops instance, an amount, and a time
    def add_hops(self, hops_helping):
        self.hops_helpings.append(hops_helping)

    def get_ingredients(self):
        self.hops = set([])
        #TODO: put in caveat that finds duplicate hops_helpings attributes.
        #and just doubles that item's aau value in the set. Whew.
        for i in range(len(self.hops_helpings)):
            self.hops.add(self.hops_helpings[i].get_attributes())
        ingredients = dict(zip([self.grain_type.name, "Hops", "Yeast",
                                "Extras"],
                               [self.grain_amount, self.hops, self.yeast,
                                self.extras]))
        return ingredients

    def brewed_me(self, brewed):
        return self.get_ingredients() == brewed.get_ingredients()

CPA = Recipe("Cincinnati Pale Ale")
recipes = [CPA]
discovered_recipes = [CPA]

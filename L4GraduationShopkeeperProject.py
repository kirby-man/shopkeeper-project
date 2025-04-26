#testing GitHub commits
import random
class Shopkeeper:
    def __init__(self, inventory):
        self.inventory = inventory

shops = ["generalStore", "petStore", "thriftStore", "farmFreshStore", "tastiesMarket", "streetMarket", "pottedPlantMarket"]
open_shops = random.sample(shops, random.randint(3, 6))
generalStoreInventory = {"Sugar": 5, "Salt": 3, "Pepper": 6, "Wheat": 2}

generalStoreShopkeeper = Shopkeeper(generalStoreInventory)

def generalStore():
    itemchoice = input("Hello and welcome to the General Store! \n We have " + str(generalStoreShopkeeper.inventory["Sugar"]) + " bundles of sugar, " + str(generalStoreShopkeeper.inventory["Salt"]) + " tins of salt, " + str(generalStoreShopkeeper.inventory["Pepper"]) + " boxes of black pepper flakes, and " + str(generalStoreShopkeeper.inventory["Wheat"]) + " bundles of wheat. \n What would you like to buy? \n").lower()
    while itemchoice not in ["sugar", "salt", "pepper", "wheat"]:
        itemchoice = ("What? Please say that again.")
    if itemchoice == "sugar":
        amount = int(input("How many do you want to buy?\n"))
        while amount not in [1, 2, 3, 4, 5]:
            amount = int(input("What? How many do you want to buy?\n"))
        print("Thank you for your purchase of " + str(amount) + " bundles of sugar. That will be $" + str(amount * 6) + ". Have a nice day!")
    elif itemchoice == "salt":
        amount = int(input("How many do you want to buy?\n"))
        while amount not in [1, 2, 3]:
            amount = int(input("What? How many do you want to buy?\n"))
        print("Thank you for your purchase of " + str(amount) + " tins of salt. That will be $" + str(amount * 4) + ". Have a nice day!")
    elif itemchoice == "pepper":
        amount = int(input("How many do you want to buy?\n"))
        while amount not in [1, 2, 3, 4, 5, 6]:
            amount = int(input("What? How many do you want to buy?\n"))
        print("Thank you for your purchase of " + str(amount) + " boxes of black pepper flakes. That will be $" + str(amount * 3) + ". Have a nice day!")
    elif itemchoice == "wheat":
        amount = int(input("How many do you want to buy?\n"))
        while amount not in [1, 2]:
            amount = int(input("What? How many do you want to buy?\n"))
        print("Thank you for your purchase of " + str(amount) + " bundles of wheat. That will be $" + str(amount * 7) + ". Have a nice day!")

def main():
    shoppingLocation = input("Hello and welcome to Shopkeeper Simulator! \n In this game, you go to shops to buy items. \n The shops currently open are " + open_shops + ".\n Which would you like to go to?")
    generalStore()



main()

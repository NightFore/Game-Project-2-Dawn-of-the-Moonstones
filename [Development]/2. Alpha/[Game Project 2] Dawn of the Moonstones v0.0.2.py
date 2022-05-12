import sys
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 7
        self.speed = 5
        self.defense = 3
        self.resistance = 2
        self.experience = 0
        self.gold = 50
        self.potion = 2
        
def main():
    print("Dawn of the Moonstones")
    print("1) Start")
    print("2) Load")
    print("3) Exit")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        #load()
        pass
    elif option == "3":
        sys.exit()
    else:
        main()

def start():
    print("What is your name?")
    option = input("-> ")
    global PlayerIG
    PlayerIG = Player(option)
    Introduction()

def Introduction():
    os.system("clear")
    print("Wake Up... %s... You have to wake up!" % PlayerIG.name)
    print("Huh...? Where am I?")
    print("I was on my way to the next town and now I wake up in the middle of this forest...")
    LvL1()

def LvL1():
    print("Name: %s" % PlayerIG.name)
    print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("Experience: %i/100" % PlayerIG.experience)
    print("Potions: %i" % PlayerIG.potion)
    print("1) Move")
    print("2) Item")
    print("3) Save")
    print("4) Exit")
    option = input("--> ")
    if option == "1":
        move()
    elif option == "2":
        item()
    elif option == "3":
        #save()
        pass
    elif option == "4":
        sys.exit()
    else:
        LvL1()







main()

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


main()

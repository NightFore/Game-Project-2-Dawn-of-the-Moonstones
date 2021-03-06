import sys
import os
import random

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

class Bandit:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 40
        self.health = self.maxhealth
        self.attack = 4
        self.speed = 1
        self.defense = 0
        self.resistance = 0
        self.gainexperience = 20
        self.gaingold = 5
BanditIG = Bandit("Bandit")

class Fighter:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 6
        self.speed = 3
        self.defense = 2
        self.resistance = 1
        self.gainexperience = 35
        self.gaingold = 25
FighterIG = Fighter("Fighter")



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
    print("Wake Up... %s... You have to wake up!" % PlayerIG.name)
    print("Huh...? Where am I?")
    print("I was on my way to the next town and now I wake up in the middle of this forest...")
    LvL1()

def LvL1():
    print("Name: %s" % PlayerIG.name)
    print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("Experience: %i/100" % PlayerIG.experience)
    print("Gold: %i" % PlayerIG.gold)
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


def move():
    global ennemy
    ennemynum = random.randint(1, 2)
    if ennemynum == 1:
        ennemy = BanditIG
    elif ennemynum == 2:
        ennemy = FighterIG
    fight()

def fight():
    print("%s        vs      %s" % (PlayerIG.name, ennemy.name))
    print("%s's Health: %i/%i       %s's Health: %i/%i" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, ennemy.name, ennemy.health, ennemy.maxhealth))
    print("Potions %i" % PlayerIG.potion)
    print("1) Attack")
    print("2) Guard")
    print("3) Potion")
    print("4) Run")
    option = input("-> ")
    if option == "1":
        attack()
    elif option == "2":
        guard()
    elif option == "3":
        usepotion()
    elif option == "4":
        run()
    else:
        fight()

def attack():
    PAttack = PlayerIG.attack
    EAttack = ennemy.attack

    #Player Phase
    ennemy.health -= PAttack
    print("%s attacks!" % PlayerIG.name)
    print("%s takes %i damage!" % (ennemy.name, PAttack))
    if ennemy.health <= 0:
        win()

    #Ennemy Phase
    PlayerIG.health -= EAttack
    print("%s attacks!" % ennemy.name)
    print("You received %i damage!" % EAttack)
    if PlayerIG.health <= 0:
        death()
        
    fight()

def guard():
    EAttack = ennemy.attack/2
    print("%s is defending" % PlayerIG.name)

    #Ennemy Phase
    PlayerIG.health -= EAttack
    print("%s attacks!" % ennemy.name)
    print("You received %i damage!" % EAttack)
    if PlayerIG.health <= 0:
        death()
        
    fight()

def usepotion():
    pass


def run():
    pass

def win():
    pass

def death():
    pass

main()

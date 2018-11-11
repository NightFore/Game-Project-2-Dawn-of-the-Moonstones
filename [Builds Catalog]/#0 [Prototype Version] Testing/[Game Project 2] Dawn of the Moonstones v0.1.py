import sys
import os
import random

weapons = {"Bronze Sword": 100, "Iron Sword": 300, "Silver Sword": 500}

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.strength = 10
        self.speed = 8
        self.defense = 5
        self.resistance = 4
        self.experience = 0
        self.gold = 0
        self.weap = ["Bronze Sword"]
        self.curweap = ["Bronze Sword"]

    def attack(self):
        attack = self.strength
        if self.curweap == "Bronze Sword":
            attack += 3
        if self.curweap == "Iron Sword":
            attack += 5
        if self.curweap == "silver Sword":
            attack += 7
        return attack
    
class Bandit:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.strength = 6
        self.speed = 2
        self.defense = 1
        self.resistance = 0
        self.experiencegain = 20
BanditIG = Bandit("Bandit")

class Fighter:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 75
        self.health = self.maxhealth
        self.strength = 8
        self.speed = 4
        self.defense = 4
        self.resistance = 1
        self.experiencegain = 30
FighterIG = Fighter("Fighter")
    

def main():
    print("Dawn of the Moonstones\n")
    print("Start Game")
    print("Load game")
    print("Exit")
    option = input("-> ")
    if option ==  "1":
        start()
    elif option == "2":
        pass
        #load() (Not implemented)
    elif option == "3":
        sys.exit()
    else:
        main()

def start():
    print("Young wanderer... What is your name?")
    option = input("--> ")
    global PlayerIG
    PlayerIG = Player(option)
    start1()

def start1():
    print("Wake Up...")
    print("Huh...? Where am I?")
    print("I was on my way to the next town and now I wake up in the middle of this forest...")
    print("Name: %s" % PlayerIG.name)
    print("Attack: %s" % PlayerIG.attack)
    print("Experience %d" % PlayerIG.experience)
    print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("Attack")
    print("Item")
    print("Trade")
    print("Wait")
    option = input("--> ")
    if option == "1":
        preattack()
    elif option == "2":
        item()
    elif option == "3":
        trade()
    elif option == "4":
        wait()

def preattack():
    global ennemy
    ennemynum = random.randint(1,2)
    print(ennemynum)
    if ennemynum == 1:
        ennemy = BanditIG
    elif ennemynum == 2:
        ennemy = FighterIG
    print("%s vs %s" % (PlayerIG.name, ennemy.name))
    print("%s's Health: %d      %s's Health: %i" % (PlayerIG.name, PlayerIG.health, ennemy.name, ennemy.health))
    print("%s's Attack: %d      %s's Attack: %i" % (PlayerIG.name, PlayerIG.attack, ennemy.name, ennemy.attack))
    print("%s's Speed: %d       %s's Speed: %i" % (PlayerIG.name, PlayerIG.speed, ennemy.name, ennemy.speed))
    print("%s's Defense: %d     %s's Defense: %i" % (PlayerIG.name, PlayerIG.defense, ennemy.name, ennemy.defense))
    print("%s's Resistance: %d  %s's Resistance: %i" % (PlayerIG.name, PlayerIG.resistance, ennemy.name, ennemy.resistance))
    print("Attack")
    print("Cancel")
    option = input("-> ")
    if option == "1":
          attack()
    elif option == "2":
          cancel()

def attack():
    PAttack = PlayerIG.attack - ennemy.defense
    EAttack = ennemy.attack - PlayerIG.defense
    # Deal Damage
    print("You deal %i damage!" % PAttack)
    print("The ennemy deals %i damage!" % EAttack)
def cancel():
    pass


def item():
    print("%s Potion" % PotionNum)
    if option =="Potion":
        PlayerIG.health += 10
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print("You drink a Potion!")
    #fight()

def win():
    PlayerIG.experience += ennemy.experiencegain
    print("You gained %s" % enemy.experiencegain)
    if PlayerIG.experience >= 100:
        #PlayerIG.experiencelvlup = 100 - PlayerIG.experience
        levelup()

def trade():
    pass

def wait():
    pass

def store():
    print("Welcome to the shop!")
    print("\nWhat would you like to buy?\n")
    print("Bronze Sword")
    print("Iron Sword")
    print("Silver Sword")
    option = input("-> ")

    if option in weapons:
        if PlayerIG.gold >= weapons[option]:
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print("You have bought %s" % option)
        else:
            print("You don't have enough gold.")
            store()
        
    else:
        print("That item does not exist")
        store()
        
main()

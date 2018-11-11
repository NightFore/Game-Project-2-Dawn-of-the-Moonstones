import sys
import os
import random
import pickle

import pygame
import time

pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dawn of Moonstones")
clock = pygame.time.Clock()

def quit_game():
    pygame.quit()
    quit()

def message_display(text, x, y, Text_Type):
    font = pygame.font.SysFont("comicsansms",50)
    TextSurf, TextRect = Text_Type(text, font)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def text_title(text, font):
    textSurface = font.render(text, True, (210,100,240))
    return textSurface, textSurface.get_rect()

def text_title_selection(text, font):
    textSurface = font.render(text, True, (95,165,244))
    return textSurface, textSurface.get_rect()













# Game Properties
weapons = {"Bronze Lance": 40, "Iron Lance":100}

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.level = 1
        self.strength = 7
        self.speed = 5
        self.defense = 3
        self.resistance = 2
        self.experience = 0
        self.gold = 500
        self.potion = 2
        self.weap = ["Bronze Lance"]
        self.curweap = "Bronze Lance"

    @property
    def attack(self):
        attack = self.strength
        if self.curweap == "Bronze Lance":
            attack += 3

        if self.curweap == "Iron Lance":
            attack += 5

        return attack
    

class Bandit:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 40
        self.health = self.maxhealth
        self.attack = 4
        self.speed = 1
        self.defense = 0
        self.resistance = 0
        self.experiencegain = 20
        self.goldgain = 5
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
        self.experiencegain = 35
        self.goldgain = 25
FighterIG = Fighter("Fighter")









def main_menu():
    print("Dawn of the Moonstones")
    print("1) Start")
    print("2) Load")
    print("3) Exit")
    message_display("Dawn of the Moonstones", (display_width/2),(display_height*0.2), text_title)
    message_display("Start", (display_width/2),(display_height*0.45), text_title_selection)
    message_display("Load", (display_width/2),(display_height*0.60), text_title_selection)
    message_display("Exit", (display_width/2),(display_height*0.75), text_title_selection)

    
    option = input("-> ")


    #Game Start
    if option == "1":
        game_intro1()

    #Load
    elif option == "2":
        if os.path.exists("savefile") == True:
            with open("savefile", "rb") as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Save File has been Loaded!")
            option = input("")
            LvL1()

        else:
            print("Save File does not exist!")
            option = input("")
            main_menu()

    #Exit
    elif option == "3":
        quit_game()
    else:
        main_menu()



def game_intro1():
    print("-What is your name?")
    option = input("-> ")
    while option == "":
        print("That doesn't seem like real name!")
        option = input("")
        print("Please, tell me your name!")
        option = input("-> ")
        
    global PlayerIG
    PlayerIG = Player(option)
    game_intro2()




def game_intro2():
    print("I see... Then, %s... you have to wake up!" % PlayerIG.name)
    option = input("")
    print("-Huh...? Where am I?")
    option = input("")
    print("I was on my way to the next town...")
    option = input("")
    print("Why am I inside a forest now?")
    option = input("")
    LvL1()




def LvL1():
    print("Name: %s" % PlayerIG.name)
    print("Weapon: %s" % PlayerIG.curweap)
    print("Potions: %i" % PlayerIG.potion)
    print("Gold: %i \n" % PlayerIG.gold)

    print("What will you do?")
    print("1) Move")
    print("2) Potion")
    print("3) Store")
    print("4) Inventory")
    print("5) Status")
    print("6) Save")
    print("7) Exit")
    option = input("--> ")

    #Move
    if option == "1":
        move()

    #Potion
    elif option == "2":
        usepotion("Move")

    #Store
    elif option == "3":
        store()

    #Inventory
    elif option == "4":
        inventory()

    #Status
    elif option == "5":
        status()

    #Save
    elif option == "6":
        with open("savefile", "wb") as f:
            pickle.dump(PlayerIG, f)
            print("Game has been saved!")
        option = input("")
        LvL1() 

    #Exit     
    elif option == "7":
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
    print("")
    print("You encountered a %s" % ennemy.name)
    option = input(" ")
    fight()






def fight():
    print("%s   vs  %s" % (PlayerIG.name, ennemy.name))
    print("%s's Health: %i/%i" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth))
    print("%s's Health: %i/%i \n" % (ennemy.name, ennemy.health, ennemy.maxhealth))
    print("Potions: %i" % PlayerIG.potion)
    print("1) Attack")
    print("2) Defend")
    print("3) Potion")
    print("4) Run")
    option = input("-> ")
    if option == "1":
        attack()
    elif option == "2":
        guard()
    elif option == "3":
        usepotion("Fighting")
    elif option == "4":
        run()
    else:
        fight()





def attack():
    PAttack = PlayerIG.attack
    EAttack = ennemy.attack
    print("")
    
    #Player Phase
    ennemy.health -= PAttack
    print("%s attacks!" % PlayerIG.name)
    print("%s takes %i damage!" % (ennemy.name, PAttack))
    if ennemy.health <= 0:
        option = input(" ")
        win()

    #Ennemy Phase
    PlayerIG.health -= EAttack
    print("%s attacks!" % ennemy.name)
    print("You received %i damage!" % EAttack)
    if PlayerIG.health <= 0:
        option = input(" ")
        death()

    option = input(" ")
       
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
       
    option = input(" ") 
    fight()



def usepotion(state):
    #No Potion
    if PlayerIG.potion == 0:
        print("You don't have any potions!")

    #Use a Potion
    else:
        PlayerIG.health += 25
        PlayerIG.potion -= 1
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print("You drank a Potion!")
        #("You recovered %i HP")

    option = input(" ")
    if state == "Fighting":
        fight()
    else:
        LvL1()



def run():
    EAttack = ennemy.attack
    RunNum = random.randint(1, 3)

    #Player Phase
    if RunNum == 1:
        print("You have successfully ran away!")
        ennemy.health = ennemy.maxhealth
        LvL1()
    else:
        print("The ennemy caught you running away!")

    #Ennemy Phase
    PlayerIG.health -= EAttack
    print("%s attacks!" % ennemy.name)
    print("You received %i damage!" % EAttack)
    if PlayerIG.health <= 0:
        death()
        
    option = input(" ")
    fight()







def LvLUP():
    if PlayerIG.experience == 100:
        PlayerIG.level += 1
        PlayerIG.experience = 0
        print("You reached Level %i!" % PlayerIG.level)

        option = input("")
        
        HP = random.randint(0,100)
        if HP <= 70:
            PlayerIG.maxhealth += 1
            print("You gaiend 1 HP!")
            
        strength = random.randint(0, 100)
        if strength <= 35:
            PlayerIG.strength += 1
            print("You gained 1 Strength!")

        speed = random.randint(0, 100)
        if speed <= 65:
            PlayerIG.speed += 1
            print("You gained 1 Speed!")

        defense = random.randint(0,100)
        if defense <= 30:
            PlayerIG.defense += 1
            print("You gained 1 Defense!")

        resistance = random.randint(0,100)
        if resistance <= 30:
            PlayerIG.resistance += 1
            print("You gained 1 Resistance!")

        option = input("")


def win():
    PlayerIG.experience += ennemy.experiencegain
    PlayerIG.gold += ennemy.goldgain
    ennemy.health = ennemy.maxhealth
    print("You felled %s!" % ennemy.name)
    print("You gained %i Experience!" % ennemy.experiencegain)
    print("You found %i Gold!" % ennemy.goldgain)
    option = input(" ")
    LvLUP()
    LvL1()

def death():
    print("The %s killed you!" % ennemy.name)
    option = input(" ")








def store():
    print("Hello Traveler! What would you like to buy?")
    print("Bronze Lance")
    print("Iron Lance")
    print("Nothing!")
    option = input("-> ")
    if option in weapons :
        if PlayerIG.gold >= weapons[option]:
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print("You bought %s" % option)
            LvL1()
            
        else:
            print("Sorry, but you don't have enough Gold!")
            option = input(" ")
            store()

    elif option == "Nothing!":
        LvL1()
        
    else:
        print("Sorry but I don't own that sort of Item!")
        option = input(" ")
        store()


def inventory():
    print("What do you want to do?")
    print("1) Equip Weapon")
    print("Cancel")
    option = input("-> ")
    if option == "1":
        equip()
    elif option == "Cancel":
        LvL1()
    else:
        inventory()

def equip():
    print("What do you want to equip?")
    for weapon in PlayerIG.weap:
        print(weapon)
    print("Cancel")
    option = input("-> ")
    if option == PlayerIG.curweap:
        print("You already have equip that weapon")
        option = (" ")
        inventory()
        
    elif option in PlayerIG.weap:
        PlayerIG.curweap = option
        print("You have equipped %s." % option)
        option = ("")
        inventory()
        
    elif option == "Cancel":
        inventory()
        
    else:
        print("You don't have %s in your inventory" % option)
        equip()



def status():
    print("")
    print("Experience: %i/100 \n" % PlayerIG.experience)
    
    print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("Attack: %i" % PlayerIG.attack)
    print("Speed: %i" % PlayerIG.speed)
    print("Defense: %i" % PlayerIG.defense)
    print("Resistance: %i \n" % PlayerIG.resistance)
    option = input("")
    LvL1()
main_menu()

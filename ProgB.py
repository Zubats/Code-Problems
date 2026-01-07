# I see Minecraft players trading itens using a system
# How could i implement a trading system using python?

#dictionaries

import random
import time

def choice():
    print("Select one of the possible choices")
    print(line)
    choice = input()
    return choice

line = 20 * '-'
x = ["An enoumous monster staring\nto the midle of your chest, \
the silver cross, his eyes are\nred as blood and you sense fear" ]

player1 = dict()
player2 = dict()
player1['name'] = 'Alex'
player2['name'] = 'Steve'
print(player1, '----',player2)
print("Player1 INSERT COIN")
go = input()
print("You're a find in a forest")
print("Between a certain possibilities of choices, you decide?")
print("A) Punch a tree")
print("B) Explore the surroundings")
print("C) See what time is it")
print(line)
choice1 = input()
choicesp1 = ["A","B","C"]
if choice1 not in choicesp1:
    choice1 = choice()

if choice1 == 'A':
    print("You got 5 pieces of wood")
    player1["wood"]= 5 
elif choice1 == 'B':
    print(line)
    time.sleep(1)
    print("You don't see much more than a lot of trees in the dense forest")
    time.sleep(1.5)
    print("But something caught your attencion, {}".format(x[random.randrange(0,len(x),1)]))

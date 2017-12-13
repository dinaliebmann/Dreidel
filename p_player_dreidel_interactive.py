'''
Simulates a dreidel game. start_game will play out a dreidel game in which
each player starts out with n pieces of gelt and will return the final
dispersion of the gelt. Game play is as follows:

Each user starts out with n pieces of gelt and places one piece each in the pot.
Player 1 spins first. There are four options for the spin:
NUN - nothing happens
GIMEL - the player gets the entire pot
HEY - the player gets half of the pot
SHIN - the player puts one piece of gelt into the pot

The game ends when the player is required to put a piece in the pot and cannot.
'''

import random

def spin(gelt, spin_pot):
    result = random.randint(1,4)
    if result is 3:
        print("Result: GIMEL")
        gelt += spin_pot
        spin_pot -= spin_pot
    elif result is 2:
        print("Result: HEY")
        gelt += spin_pot // 2
        spin_pot -= spin_pot // 2
    elif result is 1:
        print("Result: SHIN")
        gelt -= 1
        spin_pot += 1
    else:
        print("Result: NUN")
    return gelt, spin_pot

def start_game():
    pot = 0
    turn_counter = 0

    players_num = 0
    while players_num <= 0:
        players_num = int(input("How many players should there be? "))

    n = 0
    while n <= 0:
        n = int(input("How many pieces of gelt should each player start with? "))

    players = {i:n for i in range(players_num)}

    while not len([i for i in players if players[i]<0]):
        if not pot:
            pot = players_num
            players = {i: players[i]-1 for i in players}
        if len([i for i in players if players[i]<0]):
            continue
        print("\nTURN: Player {0}".format(turn_counter%players_num))
        players[turn_counter%players_num], pot = spin(players[turn_counter%players_num], pot)
        print("Pot:{0}".format(pot), players)
        turn_counter += 1
    print("Turns: {0}\tPot: {1}".format(turn_counter, pot), players)

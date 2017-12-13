'''
Simulates a dreidel game with two players. start_game will play out a dreidel game in which
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

class Player:

    def __init__(self, gelt, turn):
        self.gelt = gelt
        self.turn = turn


def spin(p, spin_pot):
    result = random.randint(1,4)
    if result is 3:
        print("Result: GIMEL")
        p.gelt += spin_pot
        spin_pot -= spin_pot
    elif result is 2:
        print("Result: HEY")
        p.gelt += spin_pot // 2
        spin_pot -= spin_pot // 2
    elif result is 1:
        print("Result: SHIN")
        p.gelt -= 1
        spin_pot += 1
    else:
        print("Result: NUN")
    p.turn = False
    return p, spin_pot

def start_game():
    n = 0
    while n <= 0:
        n = int(input("How many pieces of gelt should each player start with? "))
    pot = 0
    turn_counter = 0
    p1 = Player(n, True)
    p2 = Player(n, False)
    while not p1.gelt < 0 and not p2.gelt < 0:
        turn_counter += 1
        if not pot:
            pot = 2
            p1.gelt -= 1
            p2.gelt -= 1
        if p1.gelt < 0 or p2.gelt < 0:
            continue
        if p1.turn:
            print("TURN: P1")
            p1, pot = spin(p1, pot)
            p2.turn = True
        elif p2.turn:
            print("TURN: P2")
            p2, pot = spin(p2, pot)
            p1.turn = True
        print("Pot: {0}\tP1: {1}\tP2: {2}".format(pot, p1.gelt, p2.gelt))
    print("\nTurns:{0} Pot:{1}\tP1:{2}\tP2:{3}".format(turn_counter, pot, p1.gelt, p2.gelt))

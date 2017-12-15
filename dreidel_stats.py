'''
Simulates a dreidel game with two players. start_game will play out a dreidel game in which
each player starts out with n pieces of gelt and will return the final
dispersion of the gelt. Game play is as follows:

Each user starts out with n pieces of gelt and places one piece each in the pot.
Player 0 spins first. There are four options for the spin:
NUN - nothing happens
GIMEL - the player gets the entire pot
HEY - the player gets half of the pot
SHIN - the player puts one piece of gelt into the pot

The game ends when a player is required to put a piece in the pot and cannot.

Return statistical data for however many games are played.
'''

import random

def spin(gelt, spin_pot):
    result = random.randint(1,4)

    # GIMEL - move entirety of pot to player's gelt
    if result is 3:
        gelt += spin_pot
        spin_pot -= spin_pot

    # HEY - move half of pot to player's gelt
    elif result is 2:
        gelt += spin_pot // 2
        spin_pot -= spin_pot // 2

    # SHIN - move one piece of gelt from the player to the pot
    elif result is 1:
        gelt -= 1
        spin_pot += 1

    return gelt, spin_pot

def start_game(players_num, gelt_num, games_num=1):
    assert(players_num >= 2)
    assert(gelt_num >= 2)
    assert(games_num > 0)
    total_turns = 0
    max_turns = 0
    min_turns = 0

    # Play for games_num games
    for i in range(games_num):
        pot = 0
        turn_counter = 0

        # Start each player with gelt_num pieces of gelt
        players = {i: gelt_num for i in range(players_num)}

        # Stop when a player can no longer add gelt when required
        while not len([i for i in players if players[i]<0]):
            # Ensure pot is never empty
            if not pot:
                pot = players_num
                players = {i: players[i]-1 for i in players}
            if len([i for i in players if players[i]<0]):
                continue

            # Rotate through players during gameplay
            players[turn_counter % players_num], pot = spin(players[turn_counter % players_num], pot)
            turn_counter += 1

        # print("Turns: {0}\tPot: {1}\tPlayers:".format(turn_counter, pot), players)
        total_turns += turn_counter
        max_turns = max(max_turns, turn_counter)
        if not min_turns:
            min_turns = turn_counter
        min_turns = min(min_turns, turn_counter)

    print("Average turns: {0:.0f}\t Most turns: {1}\t "
          "Least turns: {2}".format(total_turns / games_num, max_turns, min_turns))
#!/usr/bin/env python3

# A simple TUI app to track exploration turns in old school RPGs. Specifically OSE-compatible.

import os

turn = 0
mu_light = 0
cl_light = 0
torch = 0
lantern = 0
wm_interval = 2
rest_interval = 6
pot_turns = 0
ignore_rest = False

while True:
    action = input(f"\nSelect an option: \ngo to the [n]ext turn\n[c]ast Light\nignite a [t]orch\nignite a [l]antern\ndrink a [p]otion of light\n[s]nuff out a light\ngo to [o]ptions\n[q]uit\n")

    if action == 'n':
        turn += 1
        torch -= 1
        if torch == 0:
            print('\nTorch extinguished')
        lantern -= 1
        if lantern == 0:
            print('\nLantern extinguished')
        mu_light -= 1
        if mu_light == 0:
            print('\nMagic user spell expired')
        cl_light -= 1
        if cl_light == 0:
            print('\nCleric spell expired')
        pot_turns -= 1
        if pot_turns == 0:
            print('\nPotion of light extinguished')
        if mu_light < 0:
            mu_light = 0
        if cl_light < 0:
            cl_light = 0
        if pot_turns < 0:
            pot_turns = 0
        print(f'\nCurrent turn: {turn}')
        if torch > 0:
            print(f'\nTorch turns remaining: {torch}')
        if lantern > 0:
            print(f'\nLantern turns remaining: {lantern}')
        if mu_light > 0:
            print(f'\nLight (magic user) turns remaining: {mu_light}')
        if cl_light > 0:
            print(f'\nLight (cleric) turns remaining: {cl_light}')
        if pot_turns > 0:
            print(f'\nPotion of Light turns remaining: {pot_turns}')
        if turn % wm_interval == 0:
            print('\nCheck for wandering monsters.')
        if turn % rest_interval == 0 and ignore_rest == False:
            print('\nParty must rest this turn!')
    
    elif action == 'c':
        while True:
            caster = input("\nIs this spell cast by a [c]leric or a [m]agic user? ")
            if caster == 'c':
                cl_light = 12
                break
            if caster == 'm':
                mu_light = 6
                break
            elif caster != 'c' or 'm':
                print(f'\nThat is not a valid class for casting Light, please try again.')
    elif action == 't':
        torch = 6

    elif action == 'l':
        lantern = 24
    
    elif action == 'p':
        while True:
            pot_turns = input('What is the result of the d6 roll? ')
            if pot_turns.isnumeric() == False:
                print('Sorry, that is not a valid result of a d6 roll. Try again.')
            else:
                pot_turns = int(pot_turns)
                if pot_turns > 6:
                    print('Sorry, that is not a valid result of a d6 roll. Try again.')
                else:
                    pot_turns = pot_turns + 6
                    break
    
    elif action == 'o':
        while True:
            opt_select = input('\nPlease select your desired option:\nchange [w]andering monster interval\nmodify [l]ight source times\n[c]hange resting options\n[r]eturn to the previous menu: ')
            if opt_select == 'w':
                while True:
                    temp_wm = input('How often (in number of turns) would you like to check for wandering monsters?')
                    if temp_wm.isnumeric() == False:
                        print('\nSorry, turns must be a number.')
                    else:
                        int(temp_wm)
                        wm_interval = temp_wm
                        print(f'\nInterval set to {wm_interval}')
                        break

            if opt_select == 'l':
                while True:
                    light_select = input(f'\nWould you like to modify a [t]orch, [l]antern, [s]pell, [p]otion, or [r]eturn to the previous menu? ')
                    if light_select == 't':
                        while True:
                            torch_select = input('Please enter the number of turns remaining on the torch: ')
                            if torch_select.isnumeric() == False:
                                print(f'Torch turns must be a number. Please try again.')
                            else:
                                int(torch_select)
                                torch = torch_select
                                print(f'Turns remaining set to {torch}')
                                break
                    if light_select == 'l':
                        while True:
                            lantern_select = input('\nPlease enter the number of turns remaining on the lantern: ')
                            if lantern_select.isnumeric() == False:
                                print(f'\nLantern turns must be a number. Please try again.')
                            else:
                                int(lantern_select)
                                lantern = lantern_select
                                print(f'\nTurns remaining set to {lantern}')
                                break
                    if light_select == 's':
                        while True:
                            caster_select = input('\nAre you adjusting the count for a [m]agic user or a [c]leric (or would you like to [r]eturn)?')
                            if caster_select == 'm':
                                while True:
                                    mu_temp = input('\nPlease enter the number of turns remaining on the magic user\'s spell: ')
                                    if mu_temp.isnumeric() == False:
                                        print(f'\nSpell turns must be a number. Please try again.')
                                    else:
                                        int(mu_temp)
                                        mu_light = mu_temp
                                        print(f'\nTurns remaining set to {mu_light}')
                                        break 
                            if caster_select == 'c':
                                while True:
                                    cl_temp = input('\nPlease enter the number of turns remaining on the cleric\'s spell: ')
                                    if cl_temp.isnumeric() == False:
                                        print(f'\nSpell turns must be a number. Please try again.')
                                    else:
                                        int(cl_temp)
                                        cl_light = cl_temp
                                        print(f'\nTurns remaining set to {cl_light}')
                                        break 
                            if caster_select == 'r':
                                break
                            if caster_select != 'c' or 'm' or 'r':
                                print('\nPlease select \'c\', \'m\', or \'r\' to proceed')
                    if light_select == 'p':
                        while True:
                            potion_select = input('\nPlease enter the number of turns remaining on the potion: ')
                            if potion_select.isnumeric() == False:
                                print(f'\nPotion turns must be a number. Please try again.')
                            else:
                                int(potion_select)
                                pot_turns = potion_select
                                print(f'\nTurns remaining set to {pot_turns}')
                                break
                    if light_select == 'r':
                        break
                if opt_select == 'c':
                    while True:
                        rest_select = input('\nWould you like to change rest [f]requency, [t]oggle resting, or [r]eturn to the previous menu?')
                        if rest_select == 'f':
                            rest_interval_temp = input('How frequently (in turns) would you like to be prompted to rest?')
                            if rest_interval_temp.isnumeric() == False:
                                print(f'\nRest intervals turns must be a number. Please try again.')
                            else:
                                int(rest_interval_temp)
                                rest_interval = rest_interval_temp
                                print(f'\nRest interval set to {rest_interval}')
                                break
                        if rest_select == 't':
                            if ignore_rest == False:
                                ignore_rest = True
                                print('\nNow ignoring rest requirements.')
                            if ignore_rest == True:
                                ignore_rest == False
                                print('\nNow reminding about rests.')
                        if rest_select == 'r':
                            break
                if opt_select == 'r':
                    break

    elif action == 's':
        while True:
            target_light = input('\nWould you like to snuff out a [t]orch, [l]antern, [c]leric\'s light spell, [m]agic user\'s light spell, a [p]otion of light, or [r]eturn?')
            if target_light == 't':
                torch = 0
                print('\nTorch snuffed')
            if target_light == 'l':
                lantern = 0
                print('\nLantern snuffed')
            if target_light == 'c':
                cl_light = 0
                print('\nCleric spell snuffed')    
            if target_light == 'm':
                mu_light = 0
                print('\nMagic user spell snuffed')
            if target_light == 'p':
                pot_turns = 0
                print('\nPotion of light snuffed')
            if target_light == 'r':
                break
            if target_light != 't' or 'l' or 'c' or 'm' or 'p' or 'r':
                print('\nPlease select a valid option')

    elif action == 'q':
        print(f'\nYou have quit the app. Goodbye!')
        break

    elif action != 'n' or 'c' or 't' or 'l' or 'p' or 'o' or 'q' or 's':
        print(f'\nThis is not a valid option. Please try again.')

    input('\nPress enter to continue.')
    os.system('clear')
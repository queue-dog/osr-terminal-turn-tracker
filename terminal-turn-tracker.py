#!/usr/bin/env python3

# A simple TUI app to track exploration turns in old school RPGs.

# TODO: Make this a real TUI and print current stats between turns.

import os

turnCount = 0
muLightTime = 0
clLightTime = 0
torchTime = 0
lanternTime = 0
wmInterval = 2
restInterval = 6
potionTime = 0
ignoreRest = False

# Clear the screen
if os.name == 'posix':
    os.system('clear')
if os.name == 'nt':
    os.system('cls')

action = None

while action != 'q': # Need to refigure this to not be 'while true'
    action = input(f"\nSelect an option: \ngo to the [n]ext turn\n[c]ast Light\nignite a [t]orch\nignite a [l]antern\ndrink a [p]otion of light\n[s]nuff out a light\ngo to [o]ptions\n[q]uit\n")
    match action:
        case 'n': # Top level option
            turnCount += 1 # As turnCount advances, each light timer counts down
            if torchTime > 0:
                torchTime -= 1
                print(f'\nTorch turns remaining: {torchTime}')
            elif torchTime > -1:
                torchTime -= 1
            elif torchTime == 0:
                print('\nTorch extinguished')
            if lanternTime > 0:
                lanternTime -= 1
                print(f'\nLantern turns remaining: {lanternTime}')
            elif lanternTime > -1:
                lanternTime -= 1
            elif lanternTime == 0:
                print('\nLantern extinguished')
            if muLightTime > 0:
                muLightTime -= 1
                print(f'\nMagic user spell turns remaining: {muLightTime}')
            elif muLightTime > -1:
                muLightTime -= 1
            elif muLightTime == 0:
                print('\nMagic user spell expired')
            if clLightTime > 0:
                clLightTime -= 1
                print(f'\nCleric spell turns remaining: {clLightTime}')
            elif clLightTime > -1:
                clLightTime -= 1
            elif clLightTime == 0:
                print('\nCleric spell expired')
            if potionTime > 0:
                potionTime -= 1
                print(f'\nPotion of Light turns remaining: {potionTime}')
            elif potionTime > -1:
                potionTime -= 1
            elif potionTime == 0:
                print('\nPotion of light extinguished')
            if turnCount % wmInterval == 0: # Check for monsters at the configured interval
                print('\nCheck for wandering monsters.')
            if turnCount % restInterval == 0 and ignoreRest == False: # Check rest requirements at the configured interval if rests are required
                print('\nParty must rest this turn!')
        case 'c': # Top level option, cast light spell
            while True:
                casterSelect = input("\nIs this spell cast by a [c]leric or a [m]agic user, or would you like to [r]eturn to the previous menu? ")
                match casterSelect:
                    case 'c': # Second level option
                        clLightTime = 12
                        break
                    case 'm': # Second level option
                        muLightTime = 6
                        break
                    case 'r': # Second level option
                        break
                    case _: # Second level option
                        print(f'\nThat is not a valid class for casting Light, please try again.')
        case 't': # Top level option, light torch
            torchTime = 6
        case 'l': # Top level option, light lantern
            lanternTime = 24
        case 'p': # Top level option, drink potion
            while True:
                potionTime = input('What is the result of the d6 roll? ')
                if potionTime.isnumeric() == False:
                    print('Sorry, that is not a valid result of a d6 roll. Try again.')
                else:
                    potionTime = int(potionTime)
                if potionTime > 6:
                    print('Sorry, that is not a valid result of a d6 roll. Try again.')
                else:
                    potionTime = potionTime + 6
                    break
        case 'o': # Top level option, go to options menu
            optionMenuSelect = None
            while optionMenuSelect != 'r':
                optionMenuSelect = input('\nPlease select your desired option:\nchange [w]andering monster interval\nmodify [l]ight source times\n[c]hange resting options\n[r]eturn to the previous menu: ')
                match optionMenuSelect:
                    case 'w': # Second level option, configure wandering monster checks
                            wmConfig = input('How often (in number of turns) would you like to check for wandering monsters? ')
                            if wmConfig.isnumeric() == False:
                                print('\nSorry, turns must be a number.')
                            else:
                                wmConfig = int(wmConfig)
                                wmInterval = wmConfig
                                print(f'\nInterval set to {wmInterval}')
                    case 'l': # Second level option, configure timers for 
                            lightOptionSelect = input(f'\nWould you like to modify a [t]orch, [l]antern, [s]pell, [p]otion, or [r]eturn to the previous menu? ')
                            match lightOptionSelect:
                                case 't': # Third level option, configure torch turns remaining
                                    while True:
                                        torchConfig = input('Please enter the number of turns remaining on the torch: ')
                                        if torchConfig.isnumeric() == False:
                                            print(f'Torch turns must be a number. Please try again.')
                                        else:
                                            torchConfig = int(torchConfig)
                                            torchTime = torchConfig
                                            print(f'Turns remaining set to {torchTime}')
                                case 'l': # Third level option, configure lantern turns
                                        lanternConfig = input('\nPlease enter the number of turns remaining on the lantern: ')
                                        if lanternConfig.isnumeric() == False:
                                            print(f'\nLantern turns must be a number. Please try again.')
                                        else:
                                            lanternConfig = int(lanternConfig)
                                            lanternTime = lanternConfig
                                            print(f'\nTurns remaining set to {lanternTime}')
                                case 's': # Third level options, configure spells
                                    casterLightConfig = None
                                    while casterLightConfig != 'r':
                                        casterLightConfig = input('\nAre you adjusting the count for a [m]agic user or a [c]leric (or would you like to [r]eturn)? ')
                                        match casterLightConfig:
                                            case 'm': # Fourth level option, choose MU
                                                muLightConfig = input('\nPlease enter the number of turns remaining on the magic user\'s spell: ')
                                                if muLightConfig.isnumeric() == False:
                                                    print(f'\nSpell turns must be a number. Please try again.')
                                                else:
                                                    muLightConfig = int(muLightConfig)
                                                    muLightTime = muLightConfig
                                                    print(f'\nTurns remaining set to {muLightTime}')
                                                    break 
                                            case 'c': # Fourth level option, choose cleric
                                                clLightConfig = input('\nPlease enter the number of turns remaining on the cleric\'s spell: ')
                                                if clLightConfig.isnumeric() == False:
                                                    print(f'\nSpell turns must be a number. Please try again.')
                                                else:
                                                    clLightConfig = int(clLightConfig)
                                                    clLightTime = clLightConfig
                                                    print(f'\nTurns remaining set to {clLightTime}')
                                            case 'r': # Fourth level option, return to previous
                                                pass
                                            case _:
                                                print(f'\nPlease select [c]leric or [m]agic user.')
                                case 'r': # Third level option, return to previous
                                    pass
                                case _: # Catchall
                                    print('\nPlease select \'c\', \'m\', or \'r\' to proceed')
                    case 'p': # Second level option, potion config
                        potionConfig = input('\nPlease enter the number of turns remaining on the potion: ')
                        if potionConfig.isnumeric() == False:
                            print(f'\nPotion turns must be a number. Please try again.')
                        else:
                            potionConfig = int(potionConfig)
                            potionTime = potionConfig
                            print(f'\nTurns remaining set to {potionTime}')
                            break
                    case 'r': # Second level option, return to previous menu
                        pass
                    case 'c': # Second level option, rest options
                        restOptionSelect = None
                        while restOptionSelect != 'r':
                            restOptionSelect = input('\nWould you like to change rest [f]requency, [t]oggle resting, or [r]eturn to the previous menu? ')
                            match restOptionSelect:
                                case 'f': # Third level option, frequency of rests
                                    restIntervalConfig = input('How frequently (in turns) would you like to be prompted to rest? ')
                                    if restIntervalConfig.isnumeric() == False:
                                        print(f'\nRest intervals turns must be a number. Please try again.')
                                    else:
                                        restIntervalConfig = int(restIntervalConfig)
                                        restInterval = restIntervalConfig
                                        print(f'\nRest interval set to {restInterval}')
                                case 't': # Third level option, rest toggle
                                    if ignoreRest == False:
                                        ignoreRest = True
                                        print('\nNow ignoring rest requirements.')
                                    elif ignoreRest == True:
                                        ignoreRest = False                                
                                        print('\nNow reminding about rests.')
                                case 'r': # Third level option, return to previous menu
                                    pass
                                case _:
                                    print('\nPlease select a valid option.')
        case 's': # Top level option, snuff light sources out
            snuffTarget = None
            while snuffTarget != 'r':
                snuffTarget = input('\nWould you like to snuff out a [t]orch, [l]antern, [c]leric\'s light spell, [m]agic user\'s light spell, a [p]otion of light, or [r]eturn? ')
                match snuffTarget:
                    case 't': # Second level option
                        torchTime = 0
                        print('\nTorch snuffed')
                    case 'l': # Second level option
                        lanternTime = 0
                        print('\nLantern snuffed')
                    case 'c': # Second level option
                        clLightTime = 0
                        print('\nCleric spell snuffed')    
                    case 'm': # Second level option
                        muLightTime = 0
                        print('\nMagic user spell snuffed')
                    case 'p': # Second level option
                        potionTime = 0
                        print('\nPotion of light snuffed')
                    case 'r': # Second level option
                        pass
                    case _: # Second level option
                        print('\nPlease select a valid option')
        case 'q': # Top level option
            pass
        case _: # Top level option    
            print(f'\nThis is not a valid option. Please try again.')

    if action != 'q':
        input('\nPress enter to continue.\n')

    # Clear the screen
    if action == 'q':
        if os.name == 'posix':
            os.system('clear')
        if os.name == 'nt':
            os.system('cls')
        print(f'\nYou have quit the app. Goodbye!')
    else:
        if os.name == 'posix':
            os.system('clear')
        if os.name == 'nt':
            os.system('cls')
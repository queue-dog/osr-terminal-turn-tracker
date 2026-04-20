#!/usr/bin/env python3

# A simple TUI app to track exploration turns in old school RPGs.

# TODO: properly comment shit and turn this into a proper TUI.

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

if os.name == 'posix':
    os.system('clear')
if os.name == 'nt':
    os.system('cls')
    

while True:
    action = input(f"\nSelect an option: \ngo to the [n]ext turn\n[c]ast Light\nignite a [t]orch\nignite a [l]antern\ndrink a [p]otion of light\n[s]nuff out a light\ngo to [o]ptions\n[q]uit\n")
    match action:
        case 'n':
            turnCount += 1
            torchTime -= 1
            if torchTime == 0:
                print('\nTorch extinguished')
            lanternTime -= 1
            if lanternTime == 0:
                print('\nLantern extinguished')
            muLightTime -= 1
            if muLightTime == 0:
                print('\nMagic user spell expired')
            clLightTime -= 1
            if clLightTime == 0:
                print('\nCleric spell expired')
            potionTime -= 1
            if potionTime == 0:
                print('\nPotion of light extinguished')
            if muLightTime < 0:
                muLightTime = 0
            if clLightTime < 0:
                clLightTime = 0
            if potionTime < 0:
                potionTime = 0
            print(f'\nCurrent turn: {turnCount}')
            if torchTime > 0:
                print(f'\nTorch turns remaining: {torchTime}')
            if lanternTime > 0:
                print(f'\nLantern turns remaining: {lanternTime}')
            if muLightTime > 0:
                print(f'\nLight (magic user) turns remaining: {muLightTime}')
            if clLightTime > 0:
                print(f'\nLight (cleric) turns remaining: {clLightTime}')
            if potionTime > 0:
                print(f'\nPotion of Light turns remaining: {potionTime}')
            if turnCount % wmInterval == 0:
                print('\nCheck for wandering monsters.')
            if turnCount % restInterval == 0 and ignoreRest == False:
                print('\nParty must rest this turn!')
        case 'c':
            while True:
                casterSelect = input("\nIs this spell cast by a [c]leric or a [m]agic user, or would you like to [r]eturn to the previous menu? ")
                match casterSelect:
                    case 'c':
                        clLightTime = 12
                        break
                    case 'm':
                        muLightTime = 6
                        break
                    case 'r':
                        break
                    case _:
                        print(f'\nThat is not a valid class for casting Light, please try again.')
        case 't':
            torchTime = 6
        case 'l':
            lanternTime = 24
        case 'p':
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
        case 'o':
            while True:
                optionMenuSelect = input('\nPlease select your desired option:\nchange [w]andering monster interval\nmodify [l]ight source times\n[c]hange resting options\n[r]eturn to the previous menu: ')
                match optionMenuSelect:
                    case 'w':
                        while True:
                            wmConfig = input('How often (in number of turns) would you like to check for wandering monsters? ')
                            if wmConfig.isnumeric() == False:
                                print('\nSorry, turns must be a number.')
                            else:
                                wmConfig = int(wmConfig)
                                wmInterval = wmConfig
                                print(f'\nInterval set to {wmInterval}')
                                break
                    case 'l':
                        while True:
                            lightOptionSelect = input(f'\nWould you like to modify a [t]orch, [l]antern, [s]pell, [p]otion, or [r]eturn to the previous menu? ')
                            match lightOptionSelect:
                                case 't':
                                    while True:
                                        torchConfig = input('Please enter the number of turns remaining on the torch: ')
                                        if torchConfig.isnumeric() == False:
                                            print(f'Torch turns must be a number. Please try again.')
                                        else:
                                            torchConfig = int(torchConfig)
                                            torchTime = torchConfig
                                            print(f'Turns remaining set to {torchTime}')
                                            break
                                case 'l':
                                    while True:
                                        lanternConfig = input('\nPlease enter the number of turns remaining on the lantern: ')
                                        if lanternConfig.isnumeric() == False:
                                            print(f'\nLantern turns must be a number. Please try again.')
                                        else:
                                            lanternConfig = int(lanternConfig)
                                            lanternTime = lanternConfig
                                            print(f'\nTurns remaining set to {lanternTime}')
                                            break
                                case 's':
                                    while True:
                                        casterLightConfig = input('\nAre you adjusting the count for a [m]agic user or a [c]leric (or would you like to [r]eturn)? ')
                                        match casterLightConfig:
                                            case 'm':
                                                muLightConfig = input('\nPlease enter the number of turns remaining on the magic user\'s spell: ')
                                                if muLightConfig.isnumeric() == False:
                                                    print(f'\nSpell turns must be a number. Please try again.')
                                                else:
                                                    muLightConfig = int(muLightConfig)
                                                    muLightTime = muLightConfig
                                                    print(f'\nTurns remaining set to {muLightTime}')
                                                    break 
                                            case 'c':
                                                clLightConfig = input('\nPlease enter the number of turns remaining on the cleric\'s spell: ')
                                                if clLightConfig.isnumeric() == False:
                                                    print(f'\nSpell turns must be a number. Please try again.')
                                                else:
                                                    clLightConfig = int(clLightConfig)
                                                    clLightTime = clLightConfig
                                                    print(f'\nTurns remaining set to {clLightTime}')
                                                    break 
                                            case 'r':
                                                break
                                            case _:
                                                print(f'\nPlease select [c]leric or [m]agic user.')
                                case 'r':
                                    break
                                case _:
                                    print('\nPlease select \'c\', \'m\', or \'r\' to proceed')
                    case 'p':
                        while True:
                            potionConfig = input('\nPlease enter the number of turns remaining on the potion: ')
                            if potionConfig.isnumeric() == False:
                                print(f'\nPotion turns must be a number. Please try again.')
                            else:
                                potionConfig = int(potionConfig)
                                potionTime = potionConfig
                                print(f'\nTurns remaining set to {potionTime}')
                                break
                    case 'r':
                        break
                    case 'c':
                        while True:
                            restOptionSelect = input('\nWould you like to change rest [f]requency, [t]oggle resting, or [r]eturn to the previous menu? ')
                            match restOptionSelect:
                                case 'f':
                                    restIntervalConfig = input('How frequently (in turns) would you like to be prompted to rest? ')
                                    if restIntervalConfig.isnumeric() == False:
                                        print(f'\nRest intervals turns must be a number. Please try again.')
                                    else:
                                        restIntervalConfig = int(restIntervalConfig)
                                        restInterval = restIntervalConfig
                                        print(f'\nRest interval set to {restInterval}')
                                        break
                                case 't':
                                    if ignoreRest == False:
                                        ignoreRest = True
                                        print('\nNow ignoring rest requirements.')
                                    elif ignoreRest == True:
                                        ignoreRest = False                                
                                        print('\nNow reminding about rests.')
                                case 'r':
                                    break
                                case _:
                                    print('\nPlease select a valid option.')
        case 's':
            while True:
                snuffTarget = input('\nWould you like to snuff out a [t]orch, [l]antern, [c]leric\'s light spell, [m]agic user\'s light spell, a [p]otion of light, or [r]eturn? ')
                match snuffTarget:
                    case 't':
                        torchTime = 0
                        print('\nTorch snuffed')
                    case 'l':
                        lanternTime = 0
                        print('\nLantern snuffed')
                    case 'c':
                        clLightTime = 0
                        print('\nCleric spell snuffed')    
                    case 'm':
                        muLightTime = 0
                        print('\nMagic user spell snuffed')
                    case 'p':
                        potionTime = 0
                        print('\nPotion of light snuffed')
                    case 'r':
                        break
                    case _:
                        print('\nPlease select a valid option')
        case 'q':
            print(f'\nYou have quit the app. Goodbye!')
            break
        case _:    
            print(f'\nThis is not a valid option. Please try again.')

    input('\nPress enter to continue.\n')

    if os.name == 'posix':
        os.system('clear')
    if os.name == 'nt':
        os.system('cls')
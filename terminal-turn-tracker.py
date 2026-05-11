#!/usr/bin/env python3

# A simple TUI app to track exploration turns in old school RPGs.

# TODO: Make this a real TUI and print current stats between turns.

import os
import sys
import csv

action = None
turnCount = None
muLightTime = None
clLightTime = None
torchTime = None
lanternTime = None
wmInterval = None
potionTime = None
ignoreWanderingMonsters = None
restInterval = None
ignoreRest = None

# Clear the screen
if os.name == 'posix':
    os.system('clear')
if os.name == 'nt':
    os.system('cls')

# Define functions
def getVariables():
    isFrozen = getattr(sys, 'frozen', False) # Check if we are already compiled
    if isFrozen: 
        basePath = os.path.expanduser('~')
        configDir = os.path.join(basePath, '.terminal-turn-tracker')
        os.makedirs(configDir, exist_ok=True) # Make a directory for the CSV if there isn't one already
    else:
        basePath = os.path.abspath('.')
        configDir = basePath # If we are in an IDE or not compiled, run in the local directory.
    
    global configPath
    configPath = os.path.join(configDir, 'config.csv')

    if not os.path.exists(configPath): # If the config isn't here, write it
        fieldNames = ['turnCount', 
                      'muLightTime', 
                      'clLightTime', 
                      'torchTime',
                      'lanternTime',
                      'wmInterval',
                      'ignoreWanderingMonsters',
                      'restInterval',
                      'potionTime',
                      'ignoreRest']
        with open(configPath, mode='w', newline='') as csvFile: # Default values
            csvWrite = csv.DictWriter(csvFile, fieldnames=fieldNames)
            csvWrite.writeheader()
            csvWrite.writerow({
                'turnCount': 0, 
                'muLightTime': -1, 
                'clLightTime': -1, 
                'torchTime': -1, 
                'lanternTime': -1, 
                'wmInterval': 2, 
                'ignoreWanderingMonsters': False, 
                'restInterval': 6, 
                'potionTime': -1, 
                'ignoreRest': False
            })
    
    with open(configPath, mode='r') as csvFile: # Read it in
        csvRead = csv.DictReader(csvFile)
        for row in csvRead:
            global turnCount
            turnCount = row['turnCount']
            turnCount = int(turnCount)
            global muLightTime
            muLightTime = row['muLightTime']
            muLightTime = int(muLightTime)
            global clLightTime
            clLightTime = row['clLightTime']
            clLightTime = int(clLightTime)
            global torchTime
            torchTime = row['torchTime']
            torchTime = int(torchTime)
            global lanternTime
            lanternTime = row['lanternTime']
            lanternTime = int(lanternTime)
            global wmInterval
            wmInterval = row['wmInterval']
            wmInterval = int(wmInterval)
            global ignoreWanderingMonsters
            ignoreWanderingMonsters = row['ignoreWanderingMonsters']
            if ignoreWanderingMonsters == 'False':
                ignoreWanderingMonsters = False
            else:
                ignoreWanderingMonsters = True
            global restInterval
            restInterval = row['restInterval']
            restInterval = int(restInterval)
            global potionTime
            potionTime = row['potionTime']
            potionTime = int(potionTime)
            global ignoreRest
            ignoreRest = row['ignoreRest']
            if ignoreRest == 'False':
                ignoreRest = False
            else:
                ignoreRest = True
        
def writeVariables():
    with open(configPath, mode='w', newline='') as csvFile:
        fieldNames = ['turnCount',
                      'muLightTime', 
                      'clLightTime', 
                      'torchTime',
                      'lanternTime',
                      'wmInterval',
                      'ignoreWanderingMonsters',
                      'restInterval',
                      'potionTime',
                      'ignoreRest']
        csvWrite = csv.DictWriter(csvFile, fieldnames=fieldNames)
        csvWrite.writeheader()
        csvWrite.writerow({'turnCount': turnCount, 
                           'muLightTime': muLightTime, 
                           'clLightTime': clLightTime, 
                           'torchTime': torchTime, 
                           'lanternTime': lanternTime, 
                           'wmInterval': wmInterval, 
                           'ignoreWanderingMonsters': ignoreWanderingMonsters, 
                           'restInterval': restInterval, 
                           'potionTime': potionTime, 
                           'ignoreRest': ignoreRest})
        print(f'Save complete!')

def resetAllVariables():
    global turnCount
    global muLightTime
    global clLightTime
    global torchTime
    global lanternTime
    global wmInterval
    global ignoreWanderingMonsters
    global restInterval
    global ignoreRest
    turnCount = 0
    muLightTime = -1
    clLightTime = -1
    torchTime = -1
    lanternTime = -1
    wmInterval = 2
    ignoreWanderingMonsters = False
    restInterval = 6
    ignoreRest = False 
    print('All variables set to initial state.')

def turnAdvance(): # What runs every time a turn advances
        global turnCount
        global torchTime
        global lanternTime
        global muLightTime
        global clLightTime
        global potionTime
        global wmInterval
        global restInterval
        global ignoreRest
        global ignoreWanderingMonsters
        turnCount += 1 # As turnCount advances, each light timer counts down
        print(f'\nCurrent turn: {turnCount}')
        if torchTime == 0:
            print('\nTorch extinguished!')
            torchTime -= 1
        elif torchTime > 0:
            torchTime -= 1
            print(f'\nTorch turns remaining: {torchTime}')
        if lanternTime == 0:
            print('\nLantern extinguished!')
            lanternTime -= 1
        elif lanternTime > 0:
            lanternTime -= 1
            print(f'\nLantern turns remaining: {lanternTime}')
        if muLightTime == 0:
            print('\nMagic user spell expired!')
            muLightTime -= 1
        elif muLightTime > 0:
            muLightTime -= 1
            print(f'\nMagic user spell turns remaining: {muLightTime}')
        if clLightTime == 0:
            print('\nCleric spell expired!')
            clLightTime -= 1
        elif clLightTime > 0:
            clLightTime -= 1
            print(f'\nCleric spell turns remaining: {clLightTime}')
        if potionTime == 0:
            print('\nPotion expired!')
            potionTime -= 1
        elif potionTime > 0:
            potionTime -= 1
            print(f'\nPotion turns remaining: {potionTime}')
        if turnCount % wmInterval == 0 and ignoreWanderingMonsters == False: # Check for monsters at the configured interval
            print('\nCheck for wandering monsters.')
        if turnCount % restInterval == 0 and ignoreRest == False: # Check rest requirements at the configured interval if rests are required
            print('\nParty must rest this turn!')

def castLight(): # Cast light spell
    global clLightTime
    global muLightTime
    casterSelect = None
    while casterSelect != 'r':
        casterSelect = input("\nIs this spell cast by a [c]leric or a [m]agic user, or would you like to [r]eturn to the previous menu? ")
        match casterSelect:
            case 'c': # Second level option
                clLightTime = 12
                print(f'\nSpell cast! {clLightTime} turns remaining.')
                break
            case 'm': # Second level option
                muLightTime = 6
                print(f'\nSpell cast! {muLightTime} turns remaining.')
                break
            case 'r': # Second level option
                pass
            case _: # Second level option
                print(f'\nThat is not a valid class for casting Light, please try again.')

def lightTorch(): # Light a torch
    global torchTime
    torchTime = 6
    print(f'\nTorch lit! {torchTime} turns remaining.')

def lightLantern(): # Light a lantern
    global lanternTime
    lanternTime = 24
    print(f'\nLantern lit! {lanternTime} turns remaining.')

def lightPotion(): # Drink and configure a Potion of Light
    global potionTime
    while potionTime <= 7:
        potionTime = input('\nWhat is the result of the d6 roll? ')
        if potionTime.isnumeric() == False:
            print('\nSorry, that is not a valid result of a d6 roll. Try again.')
            potionTime = 0
        else:
            potionTime = int(potionTime)
            if potionTime > 6:
                print('\nSorry, that is not a valid result of a d6 roll. Try again.')
            else:
                potionTime = potionTime + 6
                print(f'\nPotion drank! {potionTime} turns remaining.')

def optionsMenu():
    optionMenuSelect = None
    global restInterval
    global ignoreRest
    while optionMenuSelect != 'q':
        optionMenuSelect = input('\nPlease select your desired option:\nchange [w]andering monster settings\nmodify [l]ight source times\n[c]hange resting options\n[s]ave the running state\n[r]eset all trackers\n[q]uit to the previous menu: ')
        match optionMenuSelect:
            case 'w': # Second level option, configure wandering monster checks
                    wmOptions()
            case 'l': # Second level option, configure timers for light sources
                   lightOptions() 
            case 'q': # Second level option, return to previous menu
                pass
            case 's':
                writeVariables()
            case 'c': # Second level option, rest options
               restOptions() 
            case 'r':
                resetAllVariables()
            case _:
                print('Please select a valid option.')
def wmOptions(): # Configure wandering monsters. TODO: add options to disable wandering monster checks
    global wmInterval
    global ignoreWanderingMonsters
    wmOptionSelect = input('\nWould you like to change the [f]requency of wandering monsters checks, [t]oggle them on or off, or [r]eturn to a previous menu?\n\n')
    while wmOptionSelect != 'r':
        match wmOptionSelect:
            case 'f':
                wmConfigTurns = input('\nHow often (in number of turns) would you like to check for wandering monsters? ')
                if wmConfigTurns.isnumeric() == False:
                    print('\nSorry, turns must be a number.')
                else:
                    wmConfigTurns = int(wmConfigTurns)
                    wmInterval = wmConfigTurns
                    print(f'\nInterval set to {wmInterval}')
                    break
            case 't':
                if ignoreWanderingMonsters == False:
                    ignoreWanderingMonsters = True
                    print('\nNow ignoring wandering monster checks.')
                    break
                else:
                    ignoreWanderingMonsters = False
                    print('\nNow reminding about wandering monster checks.')
            case 'r':
                pass
            case _:
                print('Please select [f], [t], or [r].')

def lightOptions():
    global torchTime
    global lanternTime
    global muLightTime
    global clLightTime
    global potionTime
    lightOptionSelect = input(f'\nWould you like to modify a [t]orch, [l]antern, [s]pell, [p]otion, or [r]eturn to the previous menu? ')
    match lightOptionSelect:
        case 't': # Third level option, configure torch turns remaining
            resetTorchTime() 
        case 'l': # Third level option, configure lantern turns
            resetLanternTime() 
        case 's': # Third level options, configure spells
            resetCasterTime()
        case 'p': # Third level option, potion config
            resetPotionTime()
        case 'r': # Third level option, return to previous
            pass
        case _: # Catchall
            print('\nPlease select \'c\', \'m\', or \'r\' to proceed')

def resetPotionTime():
    global potionTime
    potionConfig = input('\nPlease enter the number of turns remaining on the potion: ')
    if potionConfig.isnumeric() == False:
        print(f'\nPotion turns must be a number. Please try again.')
    else:
        potionConfig = int(potionConfig)
        potionTime = potionConfig
        print(f'\nTurns remaining set to {potionTime}') 

def restOptions():
    global ignoreRest
    global restInterval
    restOptionSelect = None
    while restOptionSelect != 'r':
        restOptionSelect = input('\nWould you like to change rest [f]requency, [t]oggle resting, or [r]eturn to the previous menu? ')
        match restOptionSelect:
            case 'f': # Third level option, frequency of rests
                setRestFreq()            
            case 't': # Third level option, rest toggle
                toggleRest()
            case 'r': # Third level option, return to previous menu
                pass
            case _:
                print('\nPlease select a valid option.')

def setRestFreq():
    global restInterval
    restIntervalConfig = input('How frequently (in turns) would you like to be prompted to rest? ')
    if restIntervalConfig.isnumeric() == False:
        print(f'\nRest intervals turns must be a number. Please try again.')
    else:
        restIntervalConfig = int(restIntervalConfig)
        restInterval = restIntervalConfig
        print(f'\nRest interval set to {restInterval}')

def toggleRest():
    if ignoreRest == False:
        ignoreRest = True
        print('\nNow ignoring rest requirements.')
    else:
        ignoreRest = False                                
        print('\nNow reminding about rests.')

def snuffLight():
    global torchTime
    global lanternTime
    global clLightTime
    global muLightTime
    global potionTime
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

def resetTorchTime():
    global torchTime
    torchConfig = input('Please enter the number of turns remaining on the torch: ')
    if torchConfig.isnumeric() == False:
        print(f'Torch turns must be a number. Please try again.')
    else:
        torchConfig = int(torchConfig)
        torchTime = torchConfig
        print(f'Turns remaining set to {torchTime}')

def resetLanternTime():
    global lanternTime
    lanternConfig = input('Please enter the number of turns remaining on the lantern: ')
    if lanternConfig.isnumeric() == False:
        print(f'Lantern turns must be a number. Please try again.')
    else:
        lanternConfig = int(lanternConfig)
        lanternTime = lanternConfig
        print(f'Turns remaining set to {lanternTime}')

def resetCasterTime():
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
                    break
            case 'r':
                break
            case _:
                print('Please select [m]agic user or [c]leric.')

def mainApp():
    global action
    getVariables()
    while action != 'q': # Main body
        action = input(f"\nSelect an option: \ngo to the [n]ext turn\n[c]ast Light\nignite a [t]orch\nignite a [l]antern\ndrink a [p]otion of light\n[s]nuff out a light\ngo to [o]ptions\n[q]uit\n\n")
        match action:
            case 'n': # Top level option
               turnAdvance()
            case 'c': # Top level option, cast light spell
                castLight()
            case 't': # Top level option, light torch
                lightTorch()
            case 'l': # Top level option, light lantern
                lightLantern()
            case 'p': # Top level option, drink potion
                lightPotion()
            case 'o': # Top level option, go to options menu
                optionsMenu()
            case 's': # Top level option, snuff light sources out
                snuffLight()
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
            print(f'\nYou have quit the app. Goodbye!\n')
        else:
            if os.name == 'posix':
                os.system('clear')
            if os.name == 'nt':
                os.system('cls')

mainApp() # Actually run the damn thing
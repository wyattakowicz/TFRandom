import random
from os import system

''' a program that generate a random loadout to use in titanfall 2. simply
    run the program or double click it.

    requirment:
    you need python 3.7.4 or higher installed.
    tested on windows 10, but should work on other OS.'''

weapons_list = ['spitfire', #LMGs
                'L-star',
                'devotion',
                'car', #SMGs
                'volt']
ordnance_list = ['frag', 'arc', 'gravity star']

tacticaal_list = ['A-wall',
                  'cloak',
                  'grapple',
                  'stim',
                  'phase shift',
                  'holo',
                  'pulse blade']
kit_1_list = []
kit_2_list = []

while True:
    print("primary:", random.choice(weapons_list))
    print("ordnance:", random.choice(ordnance_list))
    print("tactical:", random.choice(tacticaal_list))
    input("press enter to generate a new build...")
    system("cls || clear") #to support both windows and linux

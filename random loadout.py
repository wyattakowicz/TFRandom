import random
from os import system

''' a program that generate a random loadout to use in titanfall 2. simply
    run the program or double click it. made by flying8lack.

    requirment:
    you need python 3.7.4 or higher installed.
    tested on windows 10, but should work on other OS.'''

weapons_list = ['spitfire', #LMGs
                'L-star',
                'devotion',
                'car', #SMGs
                'volt',
                'R-97',
                'alternator',
                'G2A5', #ARs
                'Hemlok',
                'R-101',
                'R-201',
                'Flatline',
                'EVA-8', #shotguns
                'Mastiff',
                'double take', #snipers
                'Karber',
                'DMR',
                'Cold war', #Grenadiers
                'EPG',
                'Softball',
                'SMR']
ordnance_list = ['frag', 'arc', 'gravity star', 'fire star', 'electric smoke', 'satchel']

secondary_list = ['RE-45', 'P2016', 'B3 Wingman']

Anti_Titan_list = ['Charge Rifle', 'MGL Mag Launcher', 'LG-97 Thunderbolt', 'Archer]
                   
tacticaal_list = ['A-wall',
                  'cloak',
                  'grapple',
                  'stim',
                  'phase shift',
                  'holo',
                  'pulse blade']
kit_1_list = ['fast regen', 'ordnance expert', 'phase embark', 'power cell']
kit_2_list = ['kill report', 'wallhang', 'hover', 'low profile', 'titan hunter']

#main loop
while True:
    print("primary:", random.choice(weapons_list))
    print("ordnance:", random.choice(ordnance_list))
    print("secondary:", random.choice(secondary_list))
    print("Anti-Titan:", random.choice(Anti_Titan_list))
    print("tactical:", random.choice(tacticaal_list))
    print("kit 1:", random.choice(kit_1_list))
    print("kit 2:", random.choice(kit_2_list))
    print() #for visual aspect
    input("press enter to generate a new build...")
    system("cls || clear") #to support both windows and linux (unsure about mac)

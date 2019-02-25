import random

def getStatblock(choices, race, cls):
    # STR,DEX,CON,INT,WIS,CHA
    block = [0,0,0,0,0,0]

    for i in range(6):
        #self.stats[i] += random.randint(6,18)
        if choices[i] > 0:
            block[i] = random.randint(14,18)
        elif choices[i] < 0:
            block[i] = random.randint(7,10)
        else:
            block[i] = random.randint(9,14)

    #print('unmodified block: {}'.format(block))
    # update stats by race
    if race == 'Dwarf':
        # CON/WIS +2 - CHA -2
        block[2] += 2
        block[4] += 2
        block[5] -= 2
    elif race == 'Elf':
        # DEX/INT +2 - CON -2
        block[1] += 2
        block[3] += 2
        block[2] -= 2
    elif race == 'Gnome':
        # CON/CHA +2 - STR -2
        block[2] += 2
        block[5] += 2
        block[0] -= 2
    elif race == 'Halfling':
        # DEX/CHA +2 - STR -2
        block[1] += 2
        block[5] += 2
        block[0] -= 2
    else:
        # ANY +2, give based on class

        # WIS classes
        if cls == 'Commoner':
            block[2] += 2
        elif cls == 'Cleric' or cls == 'Adept' or cls == 'Druid' or (cls == 'Monk' and choices[4]) or (cls == 'Paladin' and choices[4]):
            block[4] += 2
        # STR classes
        elif cls == 'Warrior' or cls == 'Fighter' or cls == 'Barbarian' or (cls == 'Paladin' and choices[0]):
            block[0] += 2
        # INT classes:
        elif cls == 'Wizard' or cls == 'Expert' or choices[3]:
            block[3] += 2
        # CHA classes:
        elif cls == 'Sorcerer' or cls == 'Aristocrat' or cls == 'Bard':
            block[5] += 2
        # DEX classes
        elif cls == 'Ranger' or cls == 'Rogue' or cls == 'Monk':
            block[1] += 2

    return block

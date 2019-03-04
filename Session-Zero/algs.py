import random

traitMap = {'loyalty':['loyal','honorable','faithful','positive','reliable','consistent','honest'],
            'compassion':['kind','empathetic','courteous','altruistic','helpful','forgiving','selfless'],
            'discipline':['diligent','calm','independent','punctual','driven','restrained'],
            'optimism':['optimistic','trusting','positive','grateful','honest','self-motivated','indomitable'],
            'tolerance':['tolerant','open-minded','patient','agreeable','respectful','kind','selfless'],
            'curiosity':['scholarly','studious','distractable','curious','present','resilient'],
            'creativity':['creative','versatile','adaptive','artistic','independent','self-actualizing','playful'],
            'anger':['short-tempered','wrathful','moody','insensitive','dominant','argumentative','merciless','harsh'],
            'greed':['greedy','miserly','short-sighted','narcissistic','dishonest','selfish'],
            'insecurity':['insecure','doubting','anxious','jealous','angry','uncommunicative','demanding'],
            'lust':['lustful','excessive','lecherous','uninhibited','flirtatious','libidinous','crude'],
            'laziness':['lazy','disinterested','oblivious','idle','stubborn','unrealistic','ungrateful'],
            'pride':['proud','stubborn','narcissistic','arrogant','independent','insecure','selfish'],
            'envy':['jealous','possessive','dependent','anxious','detached','uninhibited'],
            'intelligence':['clever','thoughtful','introverted','intellectual','verbose','quirky','neurotic','mischievous'],
            'wisdom':['wise','experienced','understanding','fair','generous','gracious','mature','observant'],
            'charisma':['charismatic','extroverted','confident','silver-tongued','attentive','inspiring','flirtatious','talkative'],
            'dexterity':['agile','quick-witted','hyperactive','reactive','adaptive','coordinated','calm'],
            'strength':['strong','willful','confident','loud','boisterous','positive','active','assertive'],
            'constitution':['hearty','quiet','resilient','stubborn','gregarious','healthy','lively']}

"""
getStatblock()
Takes the users choies of race, class, and strength/weakness.
Randomly generates a statblock based on choices, plus specific bonuses based on race/class.
Random distribution is higher if a strength, lower if a weakness.
"""
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

"""
getTraits()
Takes the user's choice of greatest strength/weakness, traits, and prior stats to generate additional traits similar to those listed.
Looks at chosen stats to help influence traits as well.
"""
def getTraits(best, worst, traits, stats):
    glength = len(traitMap[best])
    blength = len(traitMap[worst])
    traits.append(traitMap[best][0])
    traits.append(traitMap[worst][0])

    # randomly add 2-3 traits from each list, based on greatest str/wk
    for i in range(random.randint(2,3)):
        traits.append(traitMap[best][random.randint(1,glength - 1)])
        traits.append(traitMap[worst][random.randint(1,blength - 1)])

    # add more traits based on stats
    # INT
    if stats[3] >= 14:
        traits.append(traitMap['intelligence'][0])
        for i in range(random.randint(1,2)):
            traits.append(traitMap['intelligence'][random.randint(1,7)])
    elif stats[3] < 8:
        traits.append('dumb')
    else:
        traits.append('clever')

    # CHA
    if stats[5] >= 14:
        traits.append(traitMap['charisma'][0])
        for i in range(random.randint(1,2)):
            traits.append(traitMap['charisma'][random.randint(1,7)])
    elif stats[5] < 8:
        traits.append('flat')
    else:
        traits.append('personable')

    # WIS
    if stats[4] >= 14:
        traits.append(traitMap['wisdom'][0])
        for i in range(random.randint(1,2)):
            traits.append(traitMap['wisdom'][random.randint(1,7)])
    elif stats[4] < 8:
        traits.append('foolish')
    else:
        traits.append('observant')

    # STR
    if stats[0] >= 14:
        traits.append(traitMap['strength'][0])
        for i in range(random.randint(1,2)):
            traits.append(traitMap['strength'][random.randint(1,7)])
    elif stats[4] < 8:
        traits.append('weak')

    # DEX
    if stats[1] >= 14:
        traits.append(traitMap['dexterity'][0])
        for i in range(random.randint(1,2)):
            traits.append(traitMap['dexterity'][random.randint(1,6)])
    elif stats[1] < 8:
        traits.append('clumsy')
    
    # CON
    if stats[2] >= 14:
        traits.append(traitMap['constitution'][0])
        for i in range(random.randint(1,2)):
            traits.append(traitMap['constitution'][random.randint(1,6)])
    elif stats[2] < 8:
        traits.append('frail')

    # return list of traits with duplicates removed
    return list(dict.fromkeys(traits))


"""
getBackground()
Takes the user's choices of background features and motive, expanding on them to create a short textual background.
Adds new traits to the user's traits, while also expanding on some of them in the background.
"""
def getBackground(choices, traits, stats):
    return
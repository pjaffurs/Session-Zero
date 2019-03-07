import random
# algs.py
# This file holds the non member-functions used for this project, mostly for calculations and generations of stats or traits.
# It also holds several tables/mappings of strings in dicts, which in the future would be moved to a database.
# I realize this is horrible memory-inefficient and had I realized how much of this I would need earlier in the project would have absolutely put it into a DB

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
            'constitution':['hearty','quiet','resilient','stubborn','gregarious','healthy','lively'],
            'large family':['well-adjusted','sociable','loud','diplomatic','low-maintenance','open','happy'],
            'only child':['independent','sensitive','mature','over-achieving','uncompromising','stubborn','private'],
            'orphan':['self-motivating','independent','insecure','lonely','self-doubting','shy','dejected'],
            'one parent':['mature','involved','brave','accepting','angry','abrasive','maternal','open-minded'],
            'lonely':['lonely','loving','lecherous','dependent','needy','irritating','sad','hopeless','desperate'],
            'abusive':['abusive','harsh','flighty','self-destructive','depressed','needy','hypersexual','neutral','shy','defensive','paranoid'],
            'loving':['loving','happy','positive','optimistic','compassionate','polite','helpful','honest'],
            'tragic':['broken','depressed','accepting','dejected','unbreakable','unfazed','neutral','angry'],
            'peaceful':['peaceful','relaxed','calm','complacent','cooperative','neutral','detached','lazy'],
            'exhausting':['haggard','tired','lazy','busy','productive','irate','stressed','reliable','unmotivated'],
            'large city':['social','open-minded','friendly','versatile','wild','selfless','stressed','conscientious'],
            'small village':['insular','curious','adventurous','restrained','self-conscious','considerate','naive'],
            'noble palace':['privileged','inquisitive','entitled','courteous','rebellious','sheltered','lawful'],
            'religious community':['pious','insular','closed-minded','modest','rebellious','shy','chaste','nervous','orderly'],
            'slums':['resourceful','thankful','independent','stingy','selfish','resentful','vigilant','hopeful','generous'],
            'traveling':['open-minded','world-wise','experienced','confident','explorative','curious','generous'],
            'isolated area':['wild','independent','disrespectful','unruly','barbarous','uncivilized','realistic'],
            'place of learning':['studious','erudite','knowledgeable','rebellious','courteous','educated','quiet'],
            'lower class':['humble','hard working','diligent','responsible','frugal','envious','unrefined'],
            'merchant class':['ambitious','manipulative','industrious','motivated','social','dishonest','self-made'],
            'aristocrat':['scheming','sycophantic','ambitious','courtly','observant','refined','cutthroat','aloof'],
            'royalty':['affluent','audacious','haughty','educated','sheltered','naive','presumptuous','ruthless'],
            'child':['hopeful','creative','bratty','rowdy','shy','naive','observant','childish','curious'],
            'adolescent':['immature','naive','hormonal','amorous','moody','rebellious','rude','youthful'],
            'adult':['paranoid','self-centered','neurotic','stable','kind','parental','loyal','dishonest'],
            'middle-aged':['tired','stable','tranquil','stagnant','satisfied','conscientious','mature'],
            'old':['old','exhausted','experienced','helpful','cautious','depressed','lawful','settled','crochety'],
            'venerable':['wizened','crotchety','slow','ornery','disrespectful','aloof','respected','stubborn','nostalgic'],
            'immortal':['well-traveled','experienced','tired','vivacious','proud','self-sufficient','bold','heroic'],
            'true love':['honest','loyal','determined','hopeful','pure-hearted','idealistic'],
            'revenge':['lawful','loyal','retributive','disillusioned','dark','obsessive'],
            'save a life':['compassionate','merciful','good-natured','helpful','determined'],
            'wealth':['greedy','envious','cutthroat','miserly','industrious','selfish'],
            'power':['lustful','sly','ruthless','confident','unassuming','meticulous','sinister'],
            'freedom':['idealistic','repressed','courageous','preachy','rebellious'],
            'see the world':['repressed','wanderlust','naive','daring','curious'],
            'be a hero':['idealistic','naive','honorable','self-assured','good-natured','selfless'],
            'survive':['abused','repressed','distrustful','fearful','adaptive','flighty'],
            'obtain knowledge':['scholarly','resourceful','learned','studious','curious','obsessive'],
            'provide for family':['loving','maternal','selfless','determined','willful'],
            'none':['wild','unrestrained','fierce','independent','unbreakable','antisocial','self-reliant','inquisitive','closed-minded']}

skills = {'Acrobatics':1,
          'Appraise':5,
          'Bluff':5,
          'Climb':0,
          'Craft':3,
          'Diplomacy':5,
          'Disable Device':1,
          'Disguise':5,
          'Escape Artist':1,
          'Fly':1,
          'Handle Animal':5,
          'Heal':4,
          'Intimidate':5,
          'Knowledge':3,
          'Linguistics':3,
          'Perception':4,
          'Perform':5,
          'Profession':4,
          'Ride':1,
          'Sense Motive':4,
          'Sleight of Hand':1,
          'Spellcraft':3,
          'Stealth':1,
          'Survival':4,
          'Swim':0,
          'Use Magic Device':5}

classSkills = {'Adept':['Craft','Handle Animal','Heal','Knowledge','Profession','Spellcraft','Survival'],
               'Aristocrat':['Appraise', 'Bluff','Craft','Diplomacy','Disguise','Handle Animal','Intimidate','Knowledge','Linguistics','Perception','Perform','Profession','Ride','Sense Motive','Swim','Survival'],
               'Barbarian':['Acrobatics','Climb','Craft','Handle Animal','Intimidate','Knowledge','Perception','Ride','Survival','Swim'],
               'Bard':['Acrobatics','Appraise','Bluff','Climb','Craft','Diplomacy','Disguise','Escape Artist','Intimidate','Knowledge','Linguistics','Perception','Perform','Profession','Sense Motive','Sleight of Hand','Spellcraft','Stealth','Use Magic Device'],
               'Cleric':['Appraise','Craft','Diplomacy','Heal','Knowledge','Linguistics','Profession','Sense Motive','Spellcraft'],
               'Commoner':['Climb','Craft','Handle Animal','Perception','Profession','Ride','Swim'],
               'Druid':['Climb','Craft','Fly','Handle Animal','Heal','Knowledge','Perception','Profession','Ride','Spellcraft','Survival','Swim'],
               'Expert':['Appraise','Craft','Profession'],
               'Fighter':['Climb','Craft','Handle Animal','Intimidate','Knowledge','Profession','Ride','Survival','Swim'],
               'Monk':['Acrobatics','Climb','Craft','Escape Artist','Intimidate','Knowledge','Perception','Perform','Profession','Ride','Sense Motive','Stealth','Swim'],
               'Paladin':['Craft','Diplomacy','Handle Animal','Heal','Knowledge','Profession','Ride','Sense Motive','Spellcraft'],
               'Ranger':['Climb','Craft','Handle Animal','Heal','Intimidate','Knowledge','Perception','Profession','Ride','Spellcraft','Stealth','Survival','Swim'],
               'Rogue':['Acrobatics','Appraise','Bluff','Climb','Craft','Diplomacy','Disable Device','Disguise','Escape Artist','Intimidate','Knowledge','Linguistics','Perception','Perform','Profession','Sense Motive','Sleight of Hand','Stealth','Swim','Use Magic Device'],
               'Sorcerer':['Appraise','Bluff','Craft','Fly','Intimidate','Knowledge','Profession','Spellcraft','Use Magic Device'],
               'Warrior':['Climb','Craft','Handle Animal','Intimidate','Profession','Ride','Swim'],
               'Wizard':['Appraise','Craft','Fly','Knowledge','Linguistics','Profession','Spellcraft']}

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
getAdditionalTraits()
Takes the user's choices of background features and motive, expanding on them to create a short textual background.
Adds new traits to the user's traits, while also expanding on some of them in the background.
"""
def getAdditionalTraits(choices, traits, stats, cls, race):
    newTraits = []
    # choices are: family, childhood, env, social status, role model, memory, goal, age
    # role model/memory irrelevant here
    # case for each case per additional choice, background shaping character description

    # family: large family, only child, orphan, one parent, distant family, none
    current = traitMap[choices[0]]
    length = len(current) - 1
    for i in range(random.randint(0,3)):
        newTraits.append(current[random.randint(0,length)])

    # childhood
    current = traitMap[choices[1]]
    length = len(current) - 1
    for i in range(random.randint(0,3)):
        newTraits.append(current[random.randint(0,length)])

    # environment
    current = traitMap[choices[2]]
    length = len(current) - 1
    for i in range(random.randint(0,3)):
        newTraits.append(current[random.randint(0,length)])

    # social status
    current = traitMap[choices[3]]
    length = len(current) - 1
    for i in range(random.randint(0,3)):
        newTraits.append(current[random.randint(0,length)])

    # goal
    current = traitMap[choices[6]]
    length = len(current) - 1
    for i in range(random.randint(0,3)):
        newTraits.append(current[random.randint(0,length)])

    # age
    current = traitMap[choices[7]]
    length = len(current) - 1
    for i in range(random.randint(0,2)):
        newTraits.append(current[random.randint(0,length)])

    # randomness
    # add one random additional trait from a random category
    keys = traitMap.keys()
    val = keys[random.randint(0,len(keys) - 1)]
    newTraits.append(traitMap[val][random.randint(0,len(traitMap[val]) - 1)])

    return list(dict.fromkeys(newTraits))
    
"""
getSkills()
Takes the users stats and class and computes their skill modifiers.
"""
def getSkills(stats, cls):
    # TODO: add racial bonuses, class bonuses, skill points by class and distribution, personal choices (could allow changes on stat screen)
    mySkills = []
    keyList = skills.keys()
    classKeys = classSkills[cls]

    # calculate skill modifiers
    for key in keyList:
        bonus = 0
        if key in classSkills[cls]:
            bonus = 3
        mySkills.append((stats[skills[key]] - 10) // 2 + bonus)

    return mySkills


def getBackground(traits, stats, cls, race):
    return
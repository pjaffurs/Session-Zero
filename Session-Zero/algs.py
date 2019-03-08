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

ageRanges = {'Human':[(3,12),(12,18),(15,34),(35,52),(53,70),(70,110)],
             'Dwarf':[(3,20),(20,39),(40,124),(125,187),(188,249),(250,450)],
             'Elf':[(3,50),(50,109),(110,174),(175,262),(263,349),(350,750)],
             'Gnome':[(3,20),(20,39),(40,99),(100,149),(150,199),(200,500)],
             'Half-elf':[(3,15),(13,19),(20,61),(62,92),(93,124),(125,185)],
             'Half-orc':[(3,8),(9,13),(14,29),(30,44),(45,59),(60,80)],
             'Halfling':[(3,14),(13,19),(20,49),(50,74),(75,99),(100,200)]}
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

    # randomly add 0-2 traits from each list, based on greatest str/wk
    for i in range(random.randint(0,2)):
        traits.append(traitMap[best][random.randint(1,glength - 1)])
    for i in range(random.randint(0,2)):
        traits.append(traitMap[worst][random.randint(1,blength - 1)])

    # add more traits based on stats
    # INT
    if stats[3] >= 14:
        traits.append(traitMap['intelligence'][0])
        for i in range(random.randint(0,2)):
            traits.append(traitMap['intelligence'][random.randint(1,7)])
    elif stats[3] < 8:
        traits.append('dumb')

    # CHA
    if stats[5] >= 14:
        traits.append(traitMap['charisma'][0])
        for i in range(random.randint(0,2)):
            traits.append(traitMap['charisma'][random.randint(1,7)])
    elif stats[5] < 8:
        traits.append('flat')
    else:
        traits.append('personable')

    # WIS
    if stats[4] >= 14:
        traits.append(traitMap['wisdom'][0])
        for i in range(random.randint(0,2)):
            traits.append(traitMap['wisdom'][random.randint(1,7)])
    elif stats[4] < 8:
        traits.append('foolish')
    else:
        traits.append('observant')

    # STR
    if stats[0] >= 14:
        traits.append(traitMap['strength'][0])
        for i in range(random.randint(0,2)):
            traits.append(traitMap['strength'][random.randint(1,7)])
    elif stats[4] < 8:
        traits.append('weak')

    # DEX
    if stats[1] >= 14:
        traits.append(traitMap['dexterity'][0])
        for i in range(random.randint(0,2)):
            traits.append(traitMap['dexterity'][random.randint(1,6)])
    elif stats[1] < 8:
        traits.append('clumsy')
    
    # CON
    if stats[2] >= 14:
        traits.append(traitMap['constitution'][0])
        for i in range(random.randint(0,2)):
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
    keys = list(traitMap.keys())
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


def getBackground(name, traits, stats, cls, race, choices):
    # first sentence based on race and family
    if choices[0] == 'orphan' or choices[0] == 'none:':
        s = '{} was born to {} parents but '.format(name,race)
        if choices[0] == 'orphan':
            s += 'lost them at a young age, later being taken in by relatives.'
        else:
            s += 'was separated from them not long after birth and raised far away.'
    elif choices[0] == 'large family':
        s = '{} was born into a large {} family with many siblings and distant relations.'.format(name,race)
    elif choices[0] == 'one parent':
        s = '{} was born to {} parents but raised primarily by just their {}.'.format(name,race,'father' if random.randint(0,1) > 0 else 'mother')

    # second sentence based on childhood
    s += ' They had a {} childhood, '.format(choices[1])
    if choices[1] == 'happy':
        s += 'full of excitement, friendship, and joy from those around them.'
    elif choices[1] == 'lonely':
        s += 'with few to truly call their friends and fewer who gave them a second thought.'
    elif choices[1] == 'loving':
        s += 'full of all the love and support any child could ask for.'
    elif choices[1] == 'abusive':
        s += 'harsh and unforgiving as those who raised them and neglected them.'
    elif choices[1] == 'tragic':
        s += 'marred by loss of both those close to them and the true innocence of youth.'
    elif chocies[1] == 'peaceful':
        s += 'with little to do but sit back and enjoy life.'
    else:
        s += 'constantly working, following orders, and obeying those said to be above them.'

    # third sentence by environment and social class
    if choices[2] == 'large city':
        s += ' These years were spent exploring the city of their birth, with its sights and sounds and varied peoples.'
    elif choices[2] == 'noble palace':
        if choices[3] == 'aristocrat' or choices[3] == 'royalty':
            s += ' Raised in the trappings of nobility and a grand palace, they were surrounded by all the creature comfort they could want.'
        else:
            s += ' Their younger years were spent in service of nobility, seeing all the grand things they were born without.'
    elif choices[2] == 'place of learning':
        s += ' Few children have the chance to grow up in a school like {}, with such a connection to history and knowledge.'.format(name)
    elif choices[2] == 'slums':
        s += ' Whether poor or noble, growing up in the slums of a grand city can be a mixed experience amidst crime, community, and corruption.'
    elif choices[2] == 'traveling':
        s += ' As a child they saw much of the known world, traveling from place to place on ships and carts, seeing much of what it had to offer.'
    elif choices[2] == 'isolated area':
        s += ' They spent their youth far from what most would call "civilized" with only a scant few people and the local fauna to keep them company.'
    elif choices[2] == 'small village':
        s += ' Such a childhood was spent in a small, tightly-knit community, where secrets were rare and traditions followed to a tee.'
    elif choices[2] == 'religious community':
        s += ' For good or ill, {} grew up among priests and ascetics, with the tenets of faith drilled into them at every turn.'.format(name)

    # fourth sentence by social class
    if choices[3] == 'lower class':
        s += ' They had little money to spend and made do with small comforts; it was a simple existence but it was what they had.'
    elif choices[3] == 'merchant class':
        s += ' Their business was learning trade and while they lacked the power and wealth of those above them they rarely lacked as well.'
    elif choices[3] == 'aristocrat':
        s += ' As a member of the nobility, they lacked nothing and slowly learned the games noble houses play.'
    elif choices[3] == 'royalty':
        s += ' A child of the blood of lords and kings, they were surrounded by courtiers and dignitaries and shown the ways of court.'
    else:
        s += ' Raised in a successful family, they had money and power and were taught to recognize it from a young age.'

    # fifth sentence by role model
    # TODO: add more variation here, should be a bit more interesting
    s += ' Above all the people they knew, {} looked up to a {} for guidance, seeing them as the ideal to be reached.'.format(name, choices[4])
    
    # sixth sentence by memory and goal
    if choices[5] == 'death in the family' or choices[5] == "friend's death":
        s += " Because of the death of one so close to them, they were driven to "
        if choices[6] == 'true love':
            s += 'fill the hole in their heart with the power of true love.'
        elif choices[6] == 'revenge':
            s += 'avenge the death of their loved one by any means.'
        elif choices[6] == 'save a life':
            s += 'save the life of another and ensure nobody had to endure such loss again.'
        elif choices[6] == 'survive':
            s += 'escape the same fate themselves.'
        elif choices[6] == 'be a hero':
            s += 'become a hero and save lives rather than take them.'
        else:
            s += 'have the means to keep more death and misfortune from them.'
    elif choices[5] == 'first kiss':
        s += ' Their first kiss was a magical experience, leading them to '
        if choices[6] == 'true love':
            s += 'try to capture that moment of passion forever in a life partner.'
        else:
            s += 'live their life in pursuit of the same passion.'
    elif choices[5] == 'being punished' or choices[5] == 'caught stealing':
        s += ' After a harsh punishment as a child, their mind was opened to the idea that actions have consequences.'
    elif choices[5] == 'home invaded':
        s += ' Their home was invaded during their youth, resulting in '
        if choices[6] == 'revenge':
            s += 'their righteous quest for vengeance against the interlopers.'
        elif choices[6] == 'survive':
            s += 'an indomitable drive to survive, no matter the cost.'
        elif choices[6] == 'save a life' or choices[6] == 'be a hero':
            s += 'a drive to rescue those taken by the invaders.'
        elif choices[6] == 'freedom':
            s += 'the burning desire to free those repressed by the invaders and liberate their home.'
        else:
            s += 'the knowledge that one must have the means or the strength to protect what they care about.'
    elif choices[5] == 'assault':
        s += ' A childhood assault left them reeling and confused, but certain that '
        if choices[6] == 'revenge':
            s += 'the ones who caused them would suffer.'
        else:
            s += 'they must be strong enough to never let it happen again.'
    else:
        s += ' Running away from home as a youth taught them the value of stability but also the importance of discovering oneself.'

    # finally append a list of traits to the very end
    s += '\n\nOver the course of their life, {} has been known to be: '.format(name)
    for trait in traits[0:len(traits)-2]:
        s += trait + ', '
    s += 'and ' + traits[len(traits)-1] + '.'

    return s

"""
getAge()
Calculates the age for a person based on their race.
"""
def getAge(race, ageGrp):
    if ageGrp == 'child':
        r = ageRanges[race][0]
        return random.randint(r[0],r[1])
    elif ageGrp == 'adult':
        r = ageRanges[race][2]
        return random.randint(r[0],r[1])
    elif ageGrp == 'adolescent':
        r = ageRanges[race][1]
        return random.randint(r[0],r[1])
    elif ageGrp == 'middle-aged':
        r = ageRanges[race][3]
        return random.randint(r[0],r[1])
    elif ageGrp == 'old':
        r = ageRanges[race][4]
        return random.randint(r[0],r[1])
    elif ageGrp == 'venerable':
        r = ageRanges[race][5]
        return random.randint(r[0],r[1])
    else:
        r = ageRanges[race]
        return random.randint(r[0][0],r[5][1] + 200)

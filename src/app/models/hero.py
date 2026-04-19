'''
Hero.py - the Hero class
'''

from collections import Counter

class Hero:
    '''
    Heroes are crew members that you can hire.  
    Each hero has 3 skills out of the 6 major skills, 
    plus XP and Level, and one special-category ability.

    Skill List: 
    Negotiation, Command, Combat, Planning, Mechanical, Medical
    '''

    def __init__(self, image, assets):
        ''' Constructor for a Hero '''
        self.portrait = image
        self.name = assets.get("name","Anonymous")
        self.nickname = assets.get("nickname","Nobody")
        self.level = assets.get("level",1)
        self.special = assets.get("special", "Person")
        self.attributes = assets.get("attributes", "")
        self.xp = 0
        self.xp_uses = []

    def gain_xp(self, xp, attribute):
        ''' Add XP and decide if you need to level up '''
        self.xp += xp
        self.xp_uses.append(attribute)

        # Every 1000xp is a new level.
        if self.xp>= 1000:
            self.__level_up()

    def pretty_print(self):
        '''Prints a string version of the hero's information, for testing/logging purposes'''
        return f"{self.nickname} - xp {self.xp} - level {self.level} - attr {self.attributes}"

    def __level_up(self):
        '''
        This method levels the character up based on their xp gain, 
        every 1000xp = 1 level.
        '''
        while self.xp >= 1000:
            self.level += 1
            self.xp -= 1000
            self.__update_attributes()
        self.xp_uses.clear()

    def __update_attributes(self):
        '''
        Upon leveling up, we increase the attributes based on which ones the
        hero used in order to gain the xp.
        '''
        counts = Counter(self.xp_uses)

        for att in self.attributes:
            self.attributes[att] += int(10 * (counts[att] / len(self.xp_uses)))

import GlobalContanor
import Creature
import random

class Director:
    def __init__(self, levels, creatures, goal_minimum, goal_maximum):
        self.levels = levels
        self.creatures = creatures
        self.goal_minimum = goal_minimum
        self.goal_maximum = goal_maximum

    def find_level_actions(self, level):
        actions = [level.public_actions]
        if level.level_north != "":
            actions.append(level.level_north.public_actions)
        if level.level_northeast != "":
            actions.append(level.level_northeast.public_actions)
        if level.level_east != "":
            actions.append(level.level_east.public_actions)
        if level.level_southeast != "":
            actions.append(level.level_southeast.public_actions)
        if level.level_south != "":
            actions.append(level.level_south.public_actions)
        if level.level_southwest != "":
            actions.append(level.level_southwest.public_actions)
        if level.level_west != "":
            actions.append(level.level_west.public_actions)
        if level.level_northwest != "":
            actions.append(level.level_northwest.public_actions)
        if level.level_up != "":
            actions.append(level.level_up.public_actions)
        if level.level_down != "":
            actions.append(level.level_down.public_actions)
        return actions

    def set_creatures(self):
        self.creatures = []
        for i in self.levels:
            for j in i.occupants:
                if type(j) is Creature:
                    self.creatures.append(j)

    def equalize(self):
        while self.goal_minimum > len(self.creatures):
            random.choice(self.levels).occupants.append("Fill in method to make creature with")
        while self.goal_maximum < len(self.creatures):
            random.choice(self.levels).occupants.remove(type(Creature))

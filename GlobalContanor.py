import pygame
from Door import Door
from PersonalityTraits import PersonalityTraits
Compare_Door1 = Door(True, True, "", "", "Compare door 1", "", "", "")
pygame.init()
COLOR_INACTIVE = pygame.Color(100, 100, 100)
COLOR_ACTIVE = pygame.Color(255, 255, 255)
FONT = pygame.font.Font(None, 32)
WIDTH, HEIGHT = 1500, 700
time = 24
article_list = ["a", "the", "an"]
action_list = ["go", "take", "open", "drop", "close", "attack", "bar", "unbar", "lock", "unlock", "pick", "up"]
player_input = ""
player_inputted = False
action_show_text = ""
level_show_text = ""
gameTime = 0
location = ""
location_changed = True
input_char = '''abcdefghijklmnopqrstuvwxyz '''


def remove_article(string_list):
    for i in article_list:
        while i in string_list:
            string_list.remove(i)


def remove_action(string_list):
    for i in action_list:
        while i in string_list:
            string_list.remove(i)



from gupb.controller import keyboard
from gupb.controller import random
from gupb.controller.rustler import Rustler

keyboard_controller = keyboard.KeyboardController()
Rustlerer = Rustler()
CONFIGURATION = {
    'arenas': [
        'ordinary_chaos'
    ],
    'controllers': [
        #keyboard_controller,
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
        random.RandomController("Darius"),
        random.RandomController("Eliza"),
        random.RandomController("Fiodor"),
        Rustlerer,
        Rustler("Rustler4", blacklisted_letters=['M', 'A', 'S', 'C'], aggression_turn_dst = 0),
        Rustler("Rustler5", special_hidden=(22, 2), ignore_weapon=True, go_to_weapon_first=False),
        Rustler("Rustler6", ignore_weapon=True, disable_hidden_spots=True, blacklisted_letters=['C', 'B'], aggression_turn_dst = 100),
        Rustler("Rustler7", blacklisted_letters=['M', 'B', 'S', 'A'], aggression_turn_dst = 100),
        Rustler("Rustler8", blacklisted_letters=[], aggression_turn_dst = 100),
        Rustler("Rustler8E", blacklisted_letters=[], aggression_turn_dst = 100, explore=True),
        Rustler("Rustler9", blacklisted_letters=[], aggression_turn_dst = 3),
        Rustler("Rustler9E", blacklisted_letters=[], aggression_turn_dst = 3, explore=True),
        Rustler("Rustler10", blacklisted_letters=[], aggression_turn_dst = 1),
        Rustler("Rustler10E", blacklisted_letters=[], aggression_turn_dst = 1, explore=True),
        Rustler("Rustler11", blacklisted_letters=['M', 'B', 'S', 'C'], aggression_turn_dst = 100, explore=True)
    ],
    'start_balancing': False,
    'visualise': False,
    'show_sight':         Rustlerer,
    'runs_no': 100,
    'profiling_metrics': [],
}

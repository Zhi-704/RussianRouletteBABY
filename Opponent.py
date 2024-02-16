from Player import player
import time
import sys
import random
from HUD import character_timer


class opponent(player):

    def get_input(self, gun_chamber):
        number_of_lives = gun_chamber.count("LIVE")
        number_of_blanks = gun_chamber.count("BLANK")
        item_factor = len(self.items)
        total = number_of_lives + number_of_blanks + item_factor

        live_weight = number_of_lives / total
        blank_weight = number_of_blanks / total
        item_weight = item_factor / total

        aim_opponent_boundary = live_weight
        aim_yourself_boundary = live_weight + blank_weight

        rand_num = random.uniform(0, 1)
        if rand_num < aim_opponent_boundary:
            main_choice = "Aim at opponent"
        elif rand_num < aim_yourself_boundary:
            main_choice = "Aim at yourself"
        else:
            main_choice = "Use Item"

        if main_choice == "Aim at yourself":
            character_timer(
                f"\n\t{self.name} chose to aim at themselves.", 0.04)
        else:
            character_timer(f"\n\t{self.name} chose to " +
                            main_choice.lower() + ".", 0.04)
        time.sleep(1.5)
        return main_choice

    def handle_items(self):
        if len(self.items) == 0:
            print(f'\n\t{self.name} has no items!')
            time.sleep(1.5)
            return 'Go Back'
        else:
            item = random.choice(self.items)
            character_timer(f'\n\t{self.name} uses the {item}.', 0.04)
            time.sleep(1.5)
            return item

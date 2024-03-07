from Player import player
import time
import random
from HUD import character_timer


class opponent(player):

    def __init__(self, name, hearts, all_items):
        super().__init__(name, hearts, all_items)
        self.checked_live = False
        self.checked_blank = False

    def get_input(self, gun_chamber):
        # motivate opponent to shoot at player more
        number_of_lives = gun_chamber.count("LIVE") * 2
        number_of_blanks = gun_chamber.count("BLANK")
        item_factor = len(self.items)
        # if opponent has used the monocle item, push it to act on the shot
        if self.checked_live:
            number_of_lives *= 99
            self.checked_live = False
        if self.checked_blank:
            number_of_blanks += 99
            self.checked_blank = False
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

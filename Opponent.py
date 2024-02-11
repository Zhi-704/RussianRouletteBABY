from Player import player
import time
import sys


def character_timer(the_string, timer):
    for char in the_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(timer)


class opponent(player):
    def get_input(self):
        character_timer(f"{opponent.name} is thinking...", 0.04)
        time.sleep(2.5)
        return super().get_input()

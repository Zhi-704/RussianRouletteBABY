import random
from HUD import character_timer


class gun:
    def __init__(self, live, blank):
        self.chamber = []
        self.reload(live, blank)

    def reload(self, lives, blanks):
        self.chamber = ["LIVE"] * lives + ["BLANK"] * blanks
        random.shuffle(self.chamber)

    def check_chamber(self, first):
        chamber_size = len(self.chamber)
        number_of_lives = self.chamber.count("LIVE")
        number_of_blanks = self.chamber.count("BLANK")

        text = f'''
        There are {chamber_size} rounds left.
        '''
        text2 = f'''{number_of_lives} lives. {number_of_blanks} blanks.'''
        if first:
            character_timer(text)
            character_timer(text2)
        else:
            print(text)

    def check_current_bullet(self):
        current = self.chamber.pop()
        self.chamber.append(current)
        return current

    def fire(self):
        return self.chamber.pop()

    def add_bullet(self, bullet):
        if bullet == "LIVE" or bullet == "BLANK":
            self.chamber.append(bullet)
            random.shuffle(self.chamber)
        else:
            print("\n ERROR WITH ADDING BULLET \n")


if __name__ == "__main__":
    test_gun = gun(1, 3)
    print(test_gun.chamber)
    fired_bullet = test_gun.fire()
    print(f"\nThe round fired was: {fired_bullet}")
    print(test_gun.chamber)
    test_gun.add_bullet("LIVE")
    print(test_gun.chamber)
    test_gun.add_bullet("LIVE")
    print(test_gun.chamber)
    test_gun.check_chamber()

import HUD
import time
import random


class player:
    def __init__(self, name, hearts, all_items):
        self.name = name
        self.hearts = hearts
        self.handcuffed = False
        self.items = []

        self.items.append(random.choice(all_items))
        self.items.append(random.choice(all_items))
        self.items.append(random.choice(all_items))
        self.items.append(random.choice(all_items))

    def check_status(self):
        text = f'''
        {self.name}
        - Hearts Remaining: {self.hearts}
        - Items On Hand: {self.items}
'''
        print(text)

    def take_damage(self, damage):
        self.hearts -= damage

    def heal(self):
        self.hearts += 1

    def get_input(self):
        main_choice = HUD.main_menu()
        return main_choice

    def handle_items(self):
        if len(self.items) == 0:
            print('\nYou have no items!')
            time.sleep(1.5)
            return 'Go Back'
        else:
            item = HUD.item_menu(self)
            return item


if __name__ == "__main__":
    test_player = player("You", 3)
    test_player.check_status()
    test_player.take_damage(2)
    test_player.check_status()
    test_player.heal()
    test_player.check_status()
    test_player.take_damage(10)
    test_player.check_status()

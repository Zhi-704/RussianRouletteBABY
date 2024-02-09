class player:
    def __init__(self, name, hearts):
        self.name = name
        self.hearts = hearts
        self.handcuffed = False
        self.items = []

    def check_status(self):
        text = f'''
        {self.name}
        - Hearts Remaining: {self.hearts}
        - Items On Hand: {self.items}
'''
        print(text)
    
    def take_damage(self,damage):
        self.hearts -= damage
    
    def heal(self):
        self.hearts += 1

if __name__ == "__main__":
    test_player = player("You", 3)
    test_player.check_status()
    test_player.take_damage(2)
    test_player.check_status()
    test_player.heal()
    test_player.check_status()
    test_player.take_damage(10)
    test_player.check_status()


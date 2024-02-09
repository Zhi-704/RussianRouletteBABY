class Player:
    def __init__(self, name, hearts):
        self.name = name
        self.hearts = hearts
        self.handcuffed = False
        self.items = []
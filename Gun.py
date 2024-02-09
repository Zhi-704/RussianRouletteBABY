import random

class gun:
    def __init__(self, live, blank):
        self.chamber = []
        self.reload(live, blank)

    def reload(self, lives, blanks):
        self.chamber = ["LIVE"] * lives + ["BLANK"] * blanks
        random.shuffle(self.chamber)
        #print(self.chamber)

    def check_current_bullet(self):
        current = self.chamber.pop()
        self.chamber.append(current)
        return current
    
    def fire(self):
        return self.chamber.pop()
    
    def add_bullet(self,bullet):
        if bullet == "LIVE" or bullet == "BLANK":
            self.chamber.append(bullet)
            random.shuffle(self.chamber)
        else:
            print("\n ERROR WITH ADDING BULLET \n")


if __name__ == "__main__":
    test_gun = gun(1,3)
    print(test_gun.chamber)
    fired_bullet = test_gun.fire()
    print(f"\nThe round fired was: {fired_bullet}")
    print(test_gun.chamber)
    test_gun.add_bullet("LIVE")
    print(test_gun.chamber)
    
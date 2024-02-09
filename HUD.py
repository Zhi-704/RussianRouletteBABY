import time

def introduction():
    text1 = '''
Welcome to the recreation of Russian Roulette. This particular version
is inspired by the game \"Buckshot Roulette\" by Mike Klubnika. 
    '''
    text2 = '''
You will play against an opponent, taking turns to shoot each other.
The gun is loaded with both live and blank bullets.
    '''
    text3 = '''
On your turn, you can choose to shoot at your opponent or yourself. 
If you shoot yourself, you get an extra turn, regardless of the bullet.
    '''
    text4 = '''
You will both be given items to maximise your chances of winning.
Use them as you please.
    '''
    print(text1)
    time.sleep(3)
    print(text2)
    time.sleep(4.5)
    print(text3)
    time.sleep(4.5)
    print(text4)
    time.sleep(3.5)
    print("May the odds be in your favour.\n")


if __name__ == "__main__":
    introduction()
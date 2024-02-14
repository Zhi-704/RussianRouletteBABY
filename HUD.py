import time
import os
import sys
import inquirer


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
    os.system('cls')
    character_timer(text1, 0.035)
    # time.sleep(1)
    character_timer(text2, 0.035)
    # time.sleep(1)
    character_timer(text3, 0.035)
    # time.sleep(1)
    character_timer(text4, 0.035)
    # time.sleep(1)
    character_timer("\n\tMay the odds be in your favour.\n", 0.1)
    time.sleep(5)
    os.system('cls')


def fire_gun(player, bullet):
    live_text = '''

        ██████╗  █████╗ ███╗   ██╗ ██████╗ ██╗██╗
        ██╔══██╗██╔══██╗████╗  ██║██╔════╝ ██║██║
        ██████╔╝███████║██╔██╗ ██║██║  ███╗██║██║
        ██╔══██╗██╔══██║██║╚██╗██║██║   ██║╚═╝╚═╝
        ██████╔╝██║  ██║██║ ╚████║╚██████╔╝██╗██╗
        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝
                                         
'''
    blank_text = '''
        click...
'''

    os.system('cls')
    if player.name == "You":
        character_timer(f"\t{player.name} take aim....", 0.1)
    else:
        character_timer(f"\t{player.name} takes aim....", 0.1)
    time.sleep(2)
    os.system('cls')

    if bullet == "BLANK":
        print(blank_text)
        time.sleep(1)
        character_timer("\tThe round was a blank.")
        time.sleep(1.5)
    if bullet == "LIVE":
        print(live_text)
        time.sleep(1)
        character_timer("\tThe round was a live.")
        time.sleep(1.5)
    os.system('cls')


def game_over():
    print("\tThe game is now over. Thank you for playing.")
    time.sleep(5)


def character_timer(the_string, timer=0.05):
    for char in the_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(timer)


main_menu_questions = [
    inquirer.List('action', message="What do you want to do?",
                  choices=['Aim at yourself', 'Aim at opponent', 'Use Item']),
]


def main_menu():
    main_answer = inquirer.prompt(
        main_menu_questions, raise_keyboard_interrupt=True)
    return main_answer['action']


def item_menu(player):
    player.items.append('Go Back')
    item_menu_questions = [
        inquirer.List('item',
                      message="Which item are you using?",
                      choices=player.items,
                      ),
    ]

    item_answer = inquirer.prompt(
        item_menu_questions, raise_keyboard_interrupt=True)
    player.items.remove('Go Back')
    return item_answer['item']


if __name__ == "__main__":
    introduction()
    fire_gun("Squidward", "LIVE")

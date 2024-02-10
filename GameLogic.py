import inquirer
import HUD
import os
from Gun import gun
from Player import player


def initiate_game():
    Player_1 = player("You", 5)
    Player_2 = player("Squidward", 5)
    The_Gun = gun(2, 4)
    Game_Won = False

    # HUD.introduction()
    while not Game_Won:
        while True:
            os.system('cls')
            if len(The_Gun.chamber) <= 0:
                The_Gun.reload()
                print("\tThe gun has been reloaded.")

            print_game_state(Player_1, Player_2, The_Gun)

            aiming = current_turn(Player_1)
            handle_firing(aiming, Player_1, Player_2, The_Gun)
            Game_Won = check_victory(Player_1, Player_2)
            if Game_Won:
                break

            if aiming == "Aim at opponent":
                break

        if Game_Won:
            break

        while True:
            os.system('cls')
            if len(The_Gun.chamber) <= 0:
                The_Gun.reload(2, 2)
                print("\tThe gun has been reloaded.")

            print_game_state(Player_1, Player_2, The_Gun)

            aiming = current_turn(Player_2)
            handle_firing(aiming, Player_2, Player_1, The_Gun)
            Game_Won = check_victory(Player_2, Player_1)
            if Game_Won:
                break

            if aiming == "Aim at opponent":
                break

    HUD.game_over()


def print_game_state(player1, player2, loaded_gun):
    player1.check_status()
    player2.check_status()
    loaded_gun.check_chamber()


def check_victory(player1, player2):
    if player1.hearts <= 0:
        print(f"\t{player2.name} has won!")
        return True
    elif player2.hearts <= 0:
        print(f"\t{player1.name} has won!")
        return True
    else:
        return False


def handle_firing(who_was_shot, the_shooter, the_victim, the_gun):
    fired_bullet = the_gun.fire()
    HUD.fire_gun(the_shooter, fired_bullet)
    if fired_bullet == "BLANK":
        return
    elif fired_bullet == "LIVE":
        if who_was_shot == "Aim at yourself":
            the_shooter.take_damage(1)
        elif who_was_shot == "Aim at opponent":
            the_victim.take_damage(1)
        return


def current_turn(player):
    while True:
        current_move = player.get_input()
        if current_move == "Aim at yourself" or current_move == "Aim at opponent":
            return current_move


if __name__ == "__main__":
    initiate_game()

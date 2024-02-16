import HUD
from HUD import character_timer
import os
from Gun import gun
from Player import player
from Opponent import opponent
import random
import time

all_items = ['Burger', 'Handcuffs', 'Monocle',
             'Pan', 'Barrel', 'Bullet', 'Blank']
# Burger - Adds 1 Heart
# Handcuffs - Opponent Skips a Go
# Monocle - Checks Current Round
# Pan - Fires a Round Without Shooting Anyone
# Barrel - Double Damage
# Bullet - Add Live Round
# Blank - Add Blank Round

chamber_configurations = [(2, 4), (4, 2), (6, 2), (1, 3), (2, 2), (4, 3)]
turn_items = []


def initiate_game():
    Player_1 = player("You", 10, all_items)
    Player_2 = opponent("Squidward", 10, all_items)
    selected_chamber = random.choice(chamber_configurations)
    The_Gun = gun(selected_chamber[0], selected_chamber[1])
    Game_Won = False
    round_counter = 1

    HUD.introduction()
    while not Game_Won:
        if (round_counter % 3) == 0:
            character_timer("\n\tItems have been redistributed.")
            time.sleep(1)
            Player_1.items = []
            Player_2.items = []
            Player_1.items.append(random.choice(all_items))
            Player_1.items.append(random.choice(all_items))
            Player_1.items.append(random.choice(all_items))
            Player_1.items.append(random.choice(all_items))

            Player_2.items.append(random.choice(all_items))
            Player_2.items.append(random.choice(all_items))
            Player_2.items.append(random.choice(all_items))
            Player_2.items.append(random.choice(all_items))
        while True:

            aiming = current_turn(Player_1, Player_2, The_Gun)
            Game_Won = check_victory(Player_1, Player_2)

            if Game_Won:
                break

            if aiming == "Aim at opponent":
                if Player_2.handcuffed:
                    character_timer(
                        f"\n\t{Player_2.name} is handcuffed. They skip a turn.")
                    time.sleep(3)
                    Player_2.handcuffed = False
                    continue
                else:
                    break

        # Needed or it will go to opponent's turn even if player won
        if Game_Won:
            break

        while True:

            aiming = current_turn(Player_2, Player_1, The_Gun)
            Game_Won = check_victory(Player_2, Player_1)

            if Game_Won:
                break

            if aiming == "Aim at opponent":
                if Player_1.handcuffed:
                    character_timer(
                        "\n\tYou are handcuffed. Skip a turn.")
                    time.sleep(3)
                    Player_1.handcuffed = False
                    continue
                else:
                    break
        round_counter += 1
    HUD.game_over()


def print_game_state(player1, player2, loaded_gun):
    player1.check_status()
    player2.check_status()
    loaded_gun.check_chamber()


def check_victory(player1, player2):
    if player1.hearts <= 0:
        character_timer(f"\t{player2.name} has won!")
        return True
    elif player2.hearts <= 0:
        character_timer(f"\t{player1.name} have won!")
        return True
    else:
        return False


def handle_firing(who_was_shot, the_shooter, the_victim, the_gun):
    fired_bullet = the_gun.fire()
    HUD.fire_gun(the_shooter, fired_bullet)
    if fired_bullet == "LIVE":
        if who_was_shot == "Aim at yourself":
            if 'Barrel' in turn_items:
                the_shooter.take_damage(2)
            else:
                the_shooter.take_damage(1)
        elif who_was_shot == "Aim at opponent":
            if 'Barrel' in turn_items:
                the_victim.take_damage(2)
            else:
                the_victim.take_damage(1)
    if 'Barrel' in turn_items:
        turn_items.remove('Barrel')
    return


def current_turn(player1, player2, gun_in_use):
    if len(gun_in_use.chamber) <= 0:
        selected_chamber = random.choice(chamber_configurations)
        gun_in_use.reload(selected_chamber[0], selected_chamber[1])
        character_timer("\tThe gun has been reloaded.", 0.06)
        time.sleep(0.8)
    while True:
        os.system('cls')
        if player1.name == "You":
            print_game_state(player1, player2, gun_in_use)
            current_move = player1.get_input()
        else:
            print_game_state(player2, player1, gun_in_use)
            character_timer(f"\n\t{player1.name} is thinking...", 0.07)
            time.sleep(1)
            current_move = player1.get_input(gun_in_use.chamber)
        if current_move == "Aim at yourself" or current_move == "Aim at opponent":
            break
        if current_move == 'Use Item':
            current_item = player1.handle_items()
            if current_item == 'Go Back':
                continue
            else:
                player1.items.remove(current_item)
                play_item(current_item, player1, player2, gun_in_use)

    handle_firing(current_move, player1, player2, gun_in_use)
    return current_move


# Burger - Adds 1 Heart
# Handcuffs - Opponent Skips a Go
# Monocle - Checks Current Round
# Pan - Fires a Round Without Shooting Anyone
# Barrel - Double Damage
# Bullet - Add Live Round
# Blank - Add Blank Round

def play_item(item_in_use, player_using_item, victim, gun_in_use):
    if item_in_use == 'Burger':
        character_timer(
            f"\n\t{player_using_item.name} ate a burger. One heart recovered.")
        player_using_item.heal()
        time.sleep(1.5)
    elif item_in_use == 'Handcuffs':
        character_timer(
            f"\n\tHandcuffs were put on {victim.name}. Skip a turn.")
        victim.handcuffed = True
        time.sleep(1.5)
    elif item_in_use == 'Monocle':
        if player_using_item.name == 'You':
            current_bullet = gun_in_use.check_current_bullet()
            character_timer(
                "\n\tYou peer into the gun with a monocle...")
            character_timer(
                f"\n\tThe current bullet is a {current_bullet}")
            time.sleep(2)
    elif item_in_use == 'Pan':
        discard = gun_in_use.fire()
        character_timer("\n\tThe gun was fired at the pan...")
        if discard == "LIVE":
            character_timer("\n\tThe pan was shot through.")
        elif discard == "BLANK":
            character_timer("\n\tThe pan remained unscathed.")
        time.sleep(3)
    elif item_in_use == 'Barrel':
        turn_items.append(item_in_use)
        character_timer(
            "\n\tA barrel was attached to the gun. The next shot will be more potent.")
        time.sleep(2)
    elif item_in_use == 'Bullet':
        gun_in_use.add_bullet("LIVE")
        character_timer(
            f"\n\tA live bullet was added to the chamber. The chamber was shuffled.")
        time.sleep(2)
    elif item_in_use == 'Blank':
        gun_in_use.add_bullet("BLANK")
        character_timer(
            "\n\tA blank bullet was added to the chamber. The chamber was shuffled.")
        time.sleep(2)


if __name__ == "__main__":
    initiate_game()

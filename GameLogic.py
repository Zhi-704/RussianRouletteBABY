import inquirer


if __name__ == "__main__":
    main_menu_questions = [
        inquirer.List('action',
                    message="What do you want to do?",
                    choices=['Aim at yourself', 'Aim at opponent', 'Use Item'],
                ),
    ]

    item_menu_questions = [
        inquirer.List('item',
                    message="Choose an item:",
                    choices=['Handcuff', 'Saw', 'Glasses'],
                ),
    ]

    def handle_main_menu(answer):
        action = answer['action']
        if action == 'Use Item':
            item_answer = inquirer.prompt(item_menu_questions)
            print("You chose to use", item_answer['item'])
        else:
            print("You chose to", action.lower())

    # Prompt for main menu
    main_answer = inquirer.prompt(main_menu_questions, raise_keyboard_interrupt=True)

    # Handle main menu selection
    handle_main_menu(main_answer)

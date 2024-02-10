import inquirer

main_menu_questions = [
    inquirer.List('action',
                  message="What do you want to do?",
                  choices=['Aim at yourself',
                           'Aim at opponent', 'Use Item'],
                  ),
]

item_menu_questions = [
    inquirer.List('item',
                  message="Which item are you using?",
                  choices=['Handcuff', 'Saw', 'Glasses'],
                  ),
]


def handle_main_menu(answer):
    action = answer['action']

    if action == 'Use Item':
        item_answer = inquirer.prompt(item_menu_questions)
        print("You chose to use", item_answer['item'])
    else:
        print("You chose to " + action.lower() + ".")


# Prompt for main menu
main_answer = inquirer.prompt(
    main_menu_questions, raise_keyboard_interrupt=True)

# Handle main menu selection
handle_main_menu(main_answer)


# Initial list of consumable items
consumables = ['Handcuff', 'Saw', 'Glasses']

# Function to handle the item menu


def handle_item_menu():
    while True:
        item_menu_questions = [
            inquirer.List('item',
                          message="Choose an item:",
                          choices=consumables + ['Exit'],
                          ),
        ]
        item_answer = inquirer.prompt(item_menu_questions)
        if item_answer['item'] == 'Exit':
            break
        else:
            print("You chose to use", item_answer['item'])
            # Remove the consumed item from the list
            consumables.remove(item_answer['item'])

# Function to handle the main menu


def handle_main_menu():
    main_menu_questions = [
        inquirer.List('action',
                      message="What do you want to do?",
                      choices=['Shoot Yourself',
                               'Shoot Opponent', 'Use Item', 'Exit'],
                      ),
    ]
    main_answer = inquirer.prompt(main_menu_questions)
    action = main_answer['action']
    if action == 'Use Item':
        handle_item_menu()
    elif action == 'Exit':
        print("Exiting...")
    else:
        print("You chose to", action.lower())

import inquirer


if __name__ == "__main__":
    questions = [
        inquirer.List('choice',
                    message="What do you want to do?",
                    choices=['Option 1', 'Option 2', 'Option 3'],
                ),
    ]

    answers = inquirer.prompt(questions)

    print("You chose:", answers['choice'])

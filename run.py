"""
Print out the title,rules of the game then
ask the player if they want to play and to input their name
to start the game.
"""

import random

print('--------------------------------')
print("|   WORLD CAPITALS QUIZ GAME   |")
print('--------------------------------\n')
print("********************************")
print('')
print("Rules of the Quiz:\n")
print('To play answer each question and press enter!')
print('If you answer correctly you will score one point if your wrong Zero,')
print('then you will go to the next question.')
print('Your score is displayed after each question.')
print('')
print("********************************")
print("")

PLAYING = ""
while PLAYING == "":
    PLAYING = input("Do you want to play? (yes/no)  ").strip()
    if PLAYING.lower() == "no":
        print("I am sorry that you don't want to play! Have a nice day!\n")
        quit()
    elif PLAYING.lower() == "yes":
        break
    print("Not a valid answer! Please, answer yes or no!\n")
    PLAYING = ""

NAME = ""
while NAME == "":
    NAME = input('Please, enter your Name to start the game: ').strip()
    if NAME == "":
        print("Your name cannot be nothing!\n")
    elif NAME.isdigit():
        print("Your name cannot be a number!\n")
        NAME = ""
    elif not NAME.isalpha():
        print("Your name should contain only letters!\n")
        NAME = ""
    elif len(NAME) < 3:
        print("Your name should be at least 3 letters long!\n")
        NAME = ""

print("")
print(f"Hello, {NAME} have fun!\n")

# Define a dictionary that contains the countries and capitals for the quiz.
world_capital = {
        "Ireland": "Dublin",
        "Australia": "Canberra",
        "Brazil ": "Brasília",
        "Canada": "Ottawa",
        "Mauritius": "Port Louis",
        "Egypt": "Cairo",
        "France": "Paris",
        "India": "New Delhi",
        "Mexico": "Mexico City",
        "Bostwana": "Gaborone",
        "South Africa": "Pretoria",
        "Bahamas": "Nassau",
        "Qatar": "Doha",
        "Peru": "Lima",
        "Monaco": "Monaco",
        "Belgium": "Brussels",
        "China": "Beijing",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Morocco": "Rabat",
        "Bulgaria": "Sofia",
        "Croatia": "Zagreb",
        "Senegal": "Dakar",
        "Thailand": "Bangkok",
        "Lebanon": "Beirut",
        "Jamaica": "Kingston",
        "Vietnam": "Hanoi",
        "Turkey": "Ankara",
        "Uruguay": "Montevideo",
        "Indonesia": "Jakarta",
        "Fiji": "Suva",
        "Paraguay": "Asunción",
        "Brazil": "Brasilia",
        "Benin": "Porto-Novo"
    }


# Define handle_input function.

def handle_input(country):
    """
    Function is used to handle empty or invalid input from the player.
    """
    player_answer = ""
    while player_answer == "":
        player_answer = input(f"What is the capital of {country}? \n").strip()
        if player_answer == "":
            print("You did not enter anything. Please try again.\n")
        else:
            return player_answer


# Define main function to start the quiz.

def capital_quiz():
    """
    Using a for loop to iterate over each country stored in the dictionary and
    asking the player for the correct answer.
    """
    # variable for storing the player score.
    score = 0
    number_of_questions = 20

    chosen_answers = []
    count = 1
    world_countries = []
    for country in world_capital:
        world_countries.append(country)
    while count <= number_of_questions:
        while True:
            country = random.choice(world_countries)
            if country in chosen_answers:
                continue
            else:
                chosen_answers.append(country)
                break

        correct_answer = world_capital[country]
        player_answer = handle_input(country)
    # checking if the player has enter a valid answer.
        if player_answer.lower() == correct_answer.lower():
            # checking if the answer is correct.
            print("Absolutely correct!\n")
            score += 1  # incremneting the score by 1 if correct answer.
        else:
            print("I am afraid not!\n")
            # we give the correct answer to the playerif it is incorrect.
            print(f"The capital of {country} is {world_capital[country]}\n")

        # print the score.
        print(f"You SCORED {score} out of {count} questions.\n")
        count += 1


FIRST_TIME_RUN = True

# start quiz loop
while True:
    if FIRST_TIME_RUN is True:
        capital_quiz()
        FIRST_TIME_RUN = False
    else:
        # asking if the player wants to play again.
        play_again = input("Do you want to play again (yes/no)?  ").strip()
        if play_again.lower() == "yes":  # if yes the game restart.
            print("")
            print("Great, let's sharpen your knowledge.\n")
            capital_quiz()
        # if no this is the end of the game.
        elif play_again.lower() == "no":
            print("")
            print("GAME OVER...GAME OVER...GAME OVER...\n")
            print("Thanks for playing, see you next time!")
            break
        else:
            print("invalid input! Try again!\n")

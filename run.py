"""
Print out the title,rules of the game then
ask the player if they want to play and to input their name
to start the game.
"""

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
playing = input("Do you want to play?  ")
if playing.lower() != "yes":
    quit()

name = input('Cool, enter your Name to start the game: ')
print("")
print(f"Hello, {name} have fun!\n")

# Define a dictionary that contains the countries and capitals for the quiz.
world_capital = {
    "France": "Paris",
    "Bostwana": "Gaborone",
    "Spain": "Madrid",
    "Australia": "Canberra",
    "Bahamas": "Nassau",
    "Peru": "Lima",
    "Monaco": "Monaco",
    "Malaysia": "Kuala Lumpur",
    "Ireland ": "Dublin",
    "Belgium": "Brussels",
    "Mauritius": "Port Louis",
    "Italy": "Rome",
    "Vietnam ": "Hanoi",
    "Qatar": "Doha",
    "Seychelles": "Victoria",
    "Bulgaria ": "Sofia",
    "Croatia ": "Zagreb",
    "Senegal ": "Dakar",
    "Thailand ": "Bangkok",
    "Lebanon ": "Beirut"
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

    for country in world_capital:
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
        print(f"You SCORED {score} out of 20 questions.\n")  # print the score.

    # asking if the player wants to play again.
    play_again = input("Do you want to play again (yes or no)?  ")
    if play_again.lower() == "yes":  # if yes the game restart.
        print("")
        print("Great, let's sharpen your knowledge.\n")
        capital_quiz()
    else:  # if no this is the end of the game.
        print("")
        print("GAME OVER...GAME OVER...GAME OVER...\n")
        print("Thanks for playing, see you next time!")


# call the main quiz function
capital_quiz()

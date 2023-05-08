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
print("Rules of the Quiz:")
print('To play answer each questions and press enter!')
print('If you answer correctly you will score one point if wrong Zero,')
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


# Function is used to handle empty or incorrect input from the player.

def handle_input(player_answer):
    if player_answer == "":
        print("You did not enter anything. Please try again.\n")
        return False
    else:
        return True


# This function runs the main quiz game.
def capital_quiz():
    score = 0  # variable for storing the player score.

    """
    Using a for loop to iterate over each country stored in the dictionary and
    asking the player fro the correct answer.
    """
    for country in world_capital:
        player_answer = input(f'What is the capital of {country} ? : ')
        correct_answer = world_capital[country]
    #checking if the player has enter a valid answer.

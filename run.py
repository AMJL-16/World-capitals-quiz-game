"""
creation of a world capital quiz game
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

# building the dictionary with countries and capitals as a gobal variable
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

 # WORLD CAPITAL QUIZ GAME
 
The World Capitals Quiz Game is a fun and educational game that tests the player knowledge of the world's capital cities. The game presents you with a list of countries and asks you to guess the corresponding capital city.
#### The quiz game is built with Python3 and runs in the Code Institute mock terminal for Heroku.

[Live version of the quiz, here.](https://world-capitals-quiz-game.herokuapp.com/)

"C:\Users\rebec\OneDrive\Desktop\pep8 validation.png"

# How to play
- The player will be presented with the game's title and rules.
- The game will ask the player if she/he wants to play, answer yes/ 
  no.
- The game will ask the player to enter your name.
- You will be asked a series of questions, asking you to name 
  the capital city of a specific country.
- Answer each question by typing in the name of the corresponding 
  capital city.
- If the player answer a question correctly, she/he will receive  
  one point.
- if you give the wrong answer, you will receive zero points and  
  the correct answer will be displayed.
- Your score will be displayed after each questions.
- At the end of the quiz you will be asked if you want to play 
  again.


# Features

- Display of the game name and rules of the game.
- Random selection of questions each time the game is played.
- Simple command-line interface.
- Input validation and error-checking.
- Provides the player with feedback on their answer if correct or 
  incorrect. 
- Calculates and displays the player's score after each questions.
- At the end of the game the player has the choice to start a new 
  game or stop.

## Future Features

- Adding all the capitals of the world.
- Improving user experience.
- Level of difficulty.

# Testing
- Passed the code through CI PEP8 Python linter with no error.
- Tested for invalid inputs: wrong answer, space, numbers and more.
- Tested the quiz in my local terminal and in the Code Institute mock terminal.

## Bugs
Solved Bugs

- I had some problem with validation which I fixed.
- Player input wasn't working properly so I fixed it with a while loop and if 
  elif statement to check for correct validation which solve the problem.
- All the input validation folloow the same model of execution.

## Remaining bugs
- None

## Validator Testing

- Code Institute PEP8 python linter
  - No errors of syntax or indentations returned.

# Deployment 

#### This project was deployed using Code Institute's mock terminal for heroku.
- Steps for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the config var if needed
  - Set the buildpacks to python and NodeJs in that order.
  - Link the Heroku app to the repository
  - click on Deploy
 # Credits

- Code Institute for the deployment terminal.
- Code Institute for the base of the README.md
- This website for the list of capitals by countries [click here](https://www.countries-ofthe-world.com/)
- I watched and learned a lot through different tutorials:
  - W3 school for the while loops and more [click here](https://www.w3schools.com/python/python_while_loops.asp)
  - freecodecamp.org(20 Python projects, 12 python projects)
  - Tech With Tim(5 Python projects, oop tutorial)
  - programming with Nick
- Python website [click here](https://docs.python.org/)
- The book Python by Eric Matthes

# Acknowledgment

A special thank you to one of the CI student Tomislav Dukez for is help on explaining concept when I wasn't understanding it and pushing me to improve my coding skills.






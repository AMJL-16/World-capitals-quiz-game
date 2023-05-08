 # WORLD CAPITAL QUIZ GAME
 
The World Capitals Quiz Game is a fun and educational game that tests the player's knowledge of the world's capital cities. The game presents you with a list of countries and asks you to guess the corresponding capital city.
#### The quiz game is built with Python3 and runs in the Code Institute mock terminal for Heroku.

[Live version of the quiz, here.](https://world-capitals-quiz-game.herokuapp.com/)

<img width="674" alt="am i responsive " src="https://user-images.githubusercontent.com/116040510/236935363-26a66cf8-c31c-4ad1-bcfe-f74d1cd6085e.png">


# How to play
- The player will be presented with the game's title and rules.
- The game will ask the player if she/he wants to play, and answer yes/ 
  no.
- The game will ask the player to enter your name.
- You will be asked a series of questions, asking you to name 
  the capital city of a specific country.
- Answer each question by typing in the name of the corresponding 
  capital city.
- If the player answers a question correctly, she/he will receive  
  one point.
- if you give the wrong answer, you will receive zero points and  
  the correct answer will be displayed.
- Your score will be displayed after each question.
- At the end of the quiz you will be asked if you want to play 
  again.


# Features

- Display the game name and rules of the game.
- <img width="371" alt="title and rulesquiz game" src="https://user-images.githubusercontent.com/116040510/236935418-7b06e840-7f3a-45d2-b84f-c15d5a16bca5.png">

- Random selection of questions each time the game is played.
  - <img width="176" alt="random questions" src="https://user-images.githubusercontent.com/116040510/236936688-1221a831-a1e1-4913-aaa6-f6d57eb9b171.png">

- Input validation and error-checking.
  - <img width="233" alt="input validation " src="https://user-images.githubusercontent.com/116040510/236936278-1b1d3bda-973d-499f-8838-25d4cb279bb2.png">
- Provides the player with feedback on their answer if correct or 
  incorrect.
  - <img width="178" alt="random questions" src="https://user-images.githubusercontent.com/116040510/236937145-3f708dfa-7cb4-492c-b234-49ed1e063a81.png">

- Calculates and displays the player's score after each question.
  - <img width="172" alt="score " src="https://user-images.githubusercontent.com/116040510/236937386-053d2cfd-e029-419c-b9c2-3838e47dc381.png">

- At the end of the game the player has the choice to start a new 
  game or stop.
  - <img width="215" alt="end of game" src="https://user-images.githubusercontent.com/116040510/236937855-02ea501c-72e6-47ec-8670-7d8da329b5b4.png">


## Future Features

- Adding all the capitals of the world.
- Improving user experience.
- Level of difficulty.

# Testing
- Passed the code through CI PEP8 Python linter with no error.
- Tested for invalid inputs: wrong answer, space, numbers, and more.
- Tested the quiz in my local terminal and the Code Institute mock terminal.

## Bugs
Solved Bugs

- I had some problems with validation which I fixed.
- Player input wasn't working properly so I fixed it with a while loop and if 
  elif statement to check for correct validation which solves the problem.
- All the input validation follows the same model of execution.

## Remaining bugs
- None

## Validator Testing

- Code Institute PEP8 python linter
  - No errors of syntax or indentations returned.
<img width="686" alt="pep8 validation" src="https://user-images.githubusercontent.com/116040510/236935085-9883f1f0-7cdb-4c5b-9caa-c2adbf1f5357.png">

# Deployment 

#### This project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the config var if needed
  - Set the build packs to Python and NodeJs in that order.
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

A special thank you to one of the CI student Tomislav Dukez for his help in explaining concepts when I wasn't understanding them and for pushing me to improve my coding skills.






#13 Number Guessing Game Objectives:
from replit import clear
# Include an ASCII art logo.
'''
 _   _                 _                      ____                      
| \ | |_   _ _ __ ___ | |__   ___ _ __ ___   / ___| __ _ _ __ ___   ___ 
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__/ __| | |  _ / _` | '_ ` _ \ / _ \
| |\  | |_| | | | | | | |_) |  __/ |  \__ \ | |_| | (_| | | | | | |  __/
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|  |___/  \____|\__,_|_| |_| |_|\___|   '''

import random
print("Welcome to the Number Guessing Game!")
new_game_continued = True
while new_game_continued==True:
  # Allow the player to submit a guess for a number between 1 and 100.
  
  guess = int(input("Guess a number between 1 and 100): ") )
  difficulty = input("Choose a difficulty. Type 'easy'or 'hard': ")
  
  def tries():
    if difficulty =="easy":
       tries = 10
    else:
      tries = 5
    return tries
  tries = tries()
  computer = random.randint(1,100)
  #for testing
  #print(computer, tries)
   
  # Check user's guess against actual answer.
  def comparison():
    if guess < computer:
      return("Too low")
    elif guess > computer:
      return("Too high")
    elif guess == computer:
      return("very good")
  result = comparison()
  
  # number of tries, depending on difficulty
  games_continued=True
  while games_continued == True:
      if guess != computer:
        tries = tries - 1
        print(comparison())
        print ("Guess again.")
        print((f"You have {tries} attemps remaining to guess the number"))
        new_guess = int(input("Make a guess.: "))
        guess = new_guess
        if guess == computer:
           print(comparison())
           games_continued=False
           print("You Win")
      if tries == 1:
        print(comparison())
        games_continued=False
        print("You've run out of guesses, you lose.")
  
  new_game = input("Do you want to play again? Type 'y' or 'n': ")
  if new_game == 'y':
    clear()
  else :
    print("Good_bye")
    new_game_continued = False
    


 

  


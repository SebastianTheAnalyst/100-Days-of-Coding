############### Blackjack Project #####################
import random
#from replit import clear 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
users_cards = []
computers_cards = []

# dealing cards
def deal_card(number_of_cards, player):
  for card in range(number_of_cards):
    deal = random.choice(cards)
    if player == "user":
      users_cards.append(deal)
    elif player == "computer":
      computers_cards.append(deal)
      
# calculating the score     
def calculate_score(player_cards):
  score = sum(player_cards)
  if 11 in player_cards and score > 21:
    while 11 in player_cards and score > 21:
      player_cards.remove(11)
      player_cards.append(1) 
#checking for Blackjack
    if score == 21:
        game_continued = False
        return 0
    elif score > 21:
        game_continued = False
  #score = sum(player_cards)
  return score

def compare(users_count, computers_count):
  if users_count == computers_count:
    print("It`s a draw")
  elif users_count == 0:
    print("Blackjack - You Win")
  elif computers_count ==0:
    print("Blackjack - The Computer wins")
  elif users_count > 21:
    print("You Lost")
  elif computers_count >21:
     print("You Win")
  elif users_count > computers_count:
    print("You Win")
  elif  users_count < computers_count:
    print("You Lost")
  print(f"Your´re score is {users_count} and the computer has {computers_count}")
  
     
# playing the game
print("Here are your cards")
deal_card(2, "user")
print(users_cards)
print("Here are the computers cards")
deal_card(2, "computer")
print(random.choice(computers_cards))

#checking the score
game_continued = True
while game_continued is True:
  users_count=calculate_score(users_cards)
  computers_count=calculate_score(computers_cards)
  if users_count < 21:
     choice = input("Do you want to draw another card? Type 'y' or 'n'\n")
     if choice == "y":
        deal_card(1, "user")
        users_count=calculate_score(users_cards)
        print("user", users_cards, users_count)
     else:
       game_continued = False
       compare(users_count, computers_count)   
  if computers_count < 17:
    deal_card(1, "computer")
    print("computer",computers_cards, computers_count)
    result=compare(users_count, computers_count)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
clear()
play_game()
  
  
   
   
  
  




import random

new_game_continued = True

while new_game_continued:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guess = int(input("Guess a number: "))
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        tries = 10
    else:
        tries = 5

    computer = random.randint(1, 100)

    def comparison():
        if guess < computer:
            return "Too low"
        elif guess > computer:
            return "Too high"
        elif guess == computer:
            return "Congratulations! You've guessed the number!"

    result = comparison()

    games_continued = True
    while games_continued:
        if guess != computer:
            tries -= 1
            print(comparison())
            if tries == 0:
                print("You've run out of guesses. You lose.")
                games_continued = False
            else:
                print(
                    f"You have {tries} attempts remaining to guess the number."
                )
                new_guess = int(input("Make a guess: "))
                guess = new_guess
        else:
            print(comparison())
            games_continued = False

    new_game = input("Do you want to play again? Type 'y' or 'n': ")
    if new_game != 'y':
        new_game_continued = False
        print("Goodbye!")

import random


word_list = ["paper", "rock", "scissors"]
lives = 6 # Lives Counter

game_over = False # Game over variable to control the while

# User and Computer points
user_points = 0
computer_points = 0

# Start the while loop
while not game_over:
    chosen_word = random.choice(word_list)
    print("____________________________________________")
    print(f"____________Just {lives} tries ___________")   # Lives counter

    guessed_word = input("Write paper, rock, or scissors: ") # The user choice
    guessed_word.lower()
    if guessed_word == chosen_word:
        print("Equal")
        print(f"Computer word: {chosen_word}") # Print the computer choice
        print(f"User word: {guessed_word}") # Print the user choice

    elif guessed_word == "paper" and chosen_word == "rock":
        print("User got one point")
        print(f"Computer word: {chosen_word}")
        print(f"User word: {guessed_word}")
        # Add one to user points
        user_points += 1 

    elif guessed_word == "paper" and chosen_word == "scissors":
        print("Computer got one point")
        print(f"Computer word: {chosen_word}") 
        print(f"User word: {guessed_word}") 
        # Add one to computer points
        computer_points += 1 

    elif guessed_word == "rock" and chosen_word == "scissors":
        print("User got one point")
        print(f"Computer word: {chosen_word}")
        print(f"User word: {guessed_word}")
        user_points += 1

    elif guessed_word == "rock" and chosen_word == "paper":
        print("Computer got one point")
        print(f"Computer word: {chosen_word}")
        print(f"User word: {guessed_word}")
        computer_points += 1

    elif guessed_word == "scissors" and chosen_word == "paper":
        print("User got one point")
        print(f"Computer word: {chosen_word}")
        print(f"User word: {guessed_word}")
        user_points += 1

    elif guessed_word == "scissors" and chosen_word == "rock":
        print("Computer got one point")
        print(f"Computer word: {chosen_word}")
        print(f"User word: {guessed_word}")
        computer_points += 1

    else:
        lives += 1 # Add one to lives, to not lose a live when wrong entering
        print("Wrong choice")
    lives -= 1
    if lives == 0:
        game_over = True

# Printing the final result

if computer_points > user_points:
    print(f"User Points = {user_points}")
    print(f"Computer Points = {computer_points}")
    print("The final winner is COMPUTER!!")
elif computer_points < user_points:
    print(f"User Points = {user_points}")
    print(f"Computer Points = {computer_points}")
    print("The final winner is USER!!")
else:
    print(f"User Points = {user_points}")
    print(f"Computer Points = {computer_points}")
    print("Sorry, no winner!!!!")
    
    
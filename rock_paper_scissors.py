import random  # Import random for the computer's random choice
import json    # Import json to save/load high scores

# Step 1: Define possible options
choices = ['rock', 'paper', 'scissors']
short_choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

# Initialize the scores
player_score = 0
computer_score = 0

# Step 2: Get player name
player_name = input("Enter your name: ")

# Step 3: Load high scores from file (if available)
def load_high_scores():
    try:
        with open("high_scores.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Step 4: Save high scores to file
def save_high_scores(high_scores):
    with open("high_scores.json", "w") as f:
        json.dump(high_scores, f, indent=4)

# Step 5: Update high scores if player has a new high score
def update_high_scores(high_scores, player_name, player_score):
    if player_name in high_scores:
        if player_score > high_scores[player_name]:
            high_scores[player_name] = player_score
    else:
        high_scores[player_name] = player_score

# Load the existing high scores
high_scores = load_high_scores()

print(f"Welcome, {player_name}! Let's play Rock, Paper, Scissors!")
print("You can enter 'r' for rock, 'p' for paper, 's' for scissors.")
print("Press 'q' at any time to quit the game.")

# Step 6: Loop the game until the player chooses to quit
while True:
    # Step 7: Get player's choice
    player_choice = input("\nEnter your choice (rock, paper, scissors or 'r', 'p', 's') or 'q' to quit: ").lower()

    # Step 8: Allow player to quit
    if player_choice == 'q':
        print("Game Over!")
        break  # Exit the loop and quit the game

    # Step 9: Map short choices to full words
    if player_choice in short_choices:
        player_choice = short_choices[player_choice]

    # Step 10: Check if input is valid
    if player_choice not in choices:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue  # Skip to the next iteration of the loop

    # Step 11: Get computer's choice randomly
    computer_choice = random.choice(choices)

    # Step 12: Display both choices
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    # Step 13: Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 'rock':
        if computer_choice == 'scissors':
            print("You win! Rock beats Scissors.")
            player_score += 1  # Increase player's score
        else:
            print("You lose! Paper beats Rock.")
            computer_score += 1  # Increase computer's score
    elif player_choice == 'paper':
        if computer_choice == 'rock':
            print("You win! Paper beats Rock.")
            player_score += 1
        else:
            print("You lose! Scissors beat Paper.")
            computer_score += 1
    elif player_choice == 'scissors':
        if computer_choice == 'paper':
            print("You win! Scissors beat Paper.")
            player_score += 1
        else:
            print("You lose! Rock beats Scissors.")
            computer_score += 1

    # Step 14: Display the current scores
    print(f"Current Score -> {player_name}: {player_score}, Computer: {computer_score}")

# Step 15: Update high score list if player has a new high score
update_high_scores(high_scores, player_name, player_score)

# Step 16: Save the updated high scores to file
save_high_scores(high_scores)

# Step 17: Display the final score when the game ends
print("\nFinal Score:")
print(f"{player_name}: {player_score}")
print(f"Computer: {computer_score}")

# Step 18: Display all-time high scores
print("\nAll-time High Scores:")
for name, score in high_scores.items():
    print(f"{name}: {score}")


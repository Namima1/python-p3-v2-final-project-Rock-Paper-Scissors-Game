import random
from database import Database

class Game:
    def __init__(self, player):
        self.player = player  # Player dictionary with player details
        self.database = Database()  # Initialize the database

    def play(self):
        while True:
            print("\nChoose your move:")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Back to Main Menu")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 4:
                    print("Returning to the main menu...")
                    break

                if choice not in [1, 2, 3]:
                    print("Invalid choice. Please choose between 1 and 3.")
                    continue

                # Map choices to Rock, Paper, or Scissors
                player_choice = self.map_choice(choice)
                computer_choice = self.get_computer_choice()

                print(f"\nYou chose: {player_choice}")
                print(f"Computer chose: {computer_choice}")

                # Determine the outcome
                outcome = self.determine_outcome(player_choice, computer_choice)
                print(f"Result: You {outcome}!")

                # Record the result in the database
                self.record_game(player_choice, computer_choice, outcome)
            except ValueError:
                print("Invalid input. Please enter a number.")

    def map_choice(self, choice):
        # Maps the choice number to Rock, Paper, or Scissors
        if choice == 1:
            return "Rock"
        elif choice == 2:
            return "Paper"
        elif choice == 3:
            return "Scissors"

    def get_computer_choice(self):
        # Randomly generates a move for the computer
        return random.choice(["Rock", "Paper", "Scissors"])

    def determine_outcome(self, player_choice, computer_choice):
        # Determines the game result
        if player_choice == computer_choice:
            return "tied"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
            (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissors" and computer_choice == "Paper"):
            return "win"
        else:
            return "lose"

    def record_game(self, player_choice, computer_choice, outcome):
        # Saves the game results in the database
        print("\nSaving game result...")
        self.database.execute_query(
            "INSERT INTO games (player_id, player_choice, computer_choice, outcome) VALUES (?, ?, ?, ?)",
            (self.player['id'], player_choice, computer_choice, outcome)
        )
        print("Game result saved!")
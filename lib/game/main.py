from players import Player
from game import Game
from database import Database

class MainMenu:
    def __init__(self, title="Rock, Paper, Scissors Game"):
        self.title = title
        self.database = Database()
        self.database.initialize()

    def run(self):
        while True:
            print(f"\n{self.title}")
            print("1. Start Game")
            print("2. View Players")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.game_page()
            elif choice == "2":
                self.display_players()
            elif choice == "3":
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def display_players(self):
        # Display all players
        players = Player.get_all_players()
        if not players:
            print("\nNo players found. Create a new player first.")
        else:
            print("\nPlayers and Rankings:")
            for rank, player in enumerate(players, start=1):
                print(f"{rank}. {player['name']} - Wins: {player['wins']}, Games Played: {player['games_played']}")

    def game_page(self):
        # Game page where users can select or create a player
        while True:
            print("\nGame Page")
            print("1. Select Existing Player")
            print("2. Create New Player")
            print("3. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.select_player()
            elif choice == "2":
                self.create_player()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Try again.")

    def select_player(self):
        # Let users select an existing player
        players = Player.get_all_players()
        if not players:
            print("\nNo players found. Please create a new player first.")
            return

        print("\nSelect a Player:")
        for index, player in enumerate(players, start=1):
            print(f"{index}. {player['name']} - Wins: {player['wins']}, Games Played: {player['games_played']}")

        try:
            choice = int(input("Enter the player number: ")) - 1
            if 0 <= choice < len(players):
                selected_player = players[choice]
                game = Game(selected_player)  # Pass the player directly
                game.play()
            else:
                print("Invalid player number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def create_player(self):
        # Create a new player
        name = input("\nEnter the new player's name: ")
        Player.add_player(name)
        player = Player.get_player(name)
        if player:
            print(f"Player {name} created successfully!")
            game = Game(player)
            game.play()
        else:
            print(f"Could not create player '{name}'. Try again.")

if __name__ == "__main__":
    menu = MainMenu(title="Welcome to the Rock, Paper, Scissors Game")
    menu.run()
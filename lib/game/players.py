from database import Database

class Player:
    @staticmethod
    def add_player(name):
        # Add a new player to the database
        db = Database()
        try:
            db.execute_query("INSERT INTO players (name) VALUES (?)", (name,))
            print(f"Player '{name}' added successfully!")
        except Exception as e:
            print(f"Error adding player: {e}")

    @staticmethod
    def get_player(name):
        # Get a player's data by name
        db = Database()
        player = db.fetch_one("SELECT * FROM players WHERE name = ?", (name,))
        if player:
            return {
                "id": player[0],
                "name": player[1],
                "wins": Player.get_wins(player[0]),
                "games_played": Player.get_games_played(player[0]),
            }
        print(f"No player found with the name '{name}'.")
        return None

    @staticmethod
    def get_all_players():
        # Retrieve all players with their stats
        db = Database()
        players = db.fetch_all("SELECT id, name FROM players")
        player_list = []
        for player in players:
            player_list.append({
                "id": player[0],
                "name": player[1],
                "wins": Player.get_wins(player[0]),
                "games_played": Player.get_games_played(player[0]),
            })
        return sorted(player_list, key=lambda p: p['wins'], reverse=True)

    @staticmethod
    def get_wins(player_id):
        # Count total wins for a player
        db = Database()
        result = db.fetch_one("SELECT COUNT(*) FROM games WHERE player_id = ? AND outcome = 'win'", (player_id,))
        return result[0] if result else 0

    @staticmethod
    def get_games_played(player_id):
        # Count total games played by a player
        db = Database()
        result = db.fetch_one("SELECT COUNT(*) FROM games WHERE player_id = ?", (player_id,))
        return result[0] if result else 0
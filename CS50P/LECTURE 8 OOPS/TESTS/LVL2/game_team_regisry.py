class Team:
    def __init__(self, team_name, collection_players):
        self.name = team_name
        self.players = collection_players

    def add_players(self, player):
        # Case A: A single string player
        if isinstance(player, str) and player:
            self.players.append(player)
            return f"{player} has been added to the squad so now current players are:\n{self.players}"
        
        # Case B: A list of players
        elif isinstance(player, list) and player:
            added_any = False
            for play in player:
                # Validate every single item inside the list
                if isinstance(play, str) and play:
                    self.players.append(play)  # Fix 2: Use append inside the loop, not extend
                    added_any = True
            
            # Fix 1: Return ONLY after the loop finishes completely
            if added_any:
                return f"New players have been added to the squad so now current players are:\n{self.players}"
            else:
                return "Invalid!!!!!!!!!!!!!! (No valid string names found in the list)"
        
        else:
            return f"Invalid!!!!!!!!!!!!!!"

    def remove_players(self, player):
        # Case A: Removing a single string player
        if isinstance(player, str) and player and player in self.players:
            self.players.remove(player)
            return f"{player} has been removed from the squad so now current players are:\n{self.players}"
        
        # Case B: Removing a list of players (Fix 3: Added support for list removal)
        elif isinstance(player, list) and player:
            removed_any = False
            for play in player:
                if isinstance(play, str) and play in self.players:
                    self.players.remove(play)
                    removed_any = True
            
            if removed_any:
                return f"Specified players have been removed. Current players are:\n{self.players}"
            else:
                return "Invalid!!!!!!!!!!!!!! (None of those players were in the squad)"
        
        else:
            return f"Invalid!!!!!!!!!!!!!!"

    def display(self):
        return f"Team name: {self.name}, collection of players: {self.players}"


# --- Execution Tests ---
team1 = Team("Lions", ["John", "Mike", "Sarah"])
team2 = Team("Tigers", ["Alice", "Bob", "Charlie"])
team3 = Team("Eagles", ["David", "Emma", "Frank"])

print("--- Testing Additions ---")
print(team1.add_players("Mike"))
print(team2.add_players(["sabur", "harry", "diokpa", "ekene", "parach", "chigozie", "delight"]))
print(team3.add_players([0, 1, 2, 3])) 
print(team3.add_players(0))            

print("\n--- Testing Removals ---")
print(team1.remove_players("Mike"))
print(team2.remove_players(["ekene", "harry"]))  # Works perfectly now!
print(team3.remove_players(1))

print("\n--- Final Display States ---")
print(team1.display())
print(team2.display())
print(team3.display())

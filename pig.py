import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll(self):
        return random.randint(1, self.sides)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f"{self.name} (Score: {self.score})"

class PigGame:
    def __init__(self, player1_name, player2_name, winning_score=100):
        self.die = Die()
        self.players = [Player(player1_name), Player(player2_name)]
        self.current_player_index = 0
        self.winning_score = winning_score
        self.turn_total = 0

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
        self.turn_total = 0

    def roll_die(self):
        roll = self.die.roll()
        print(f"{self.get_current_player().name} rolled a {roll}")
        if roll == 1:
            print(f"Rolled a 1! No points added. Switching to the other player.")
            self.switch_player()
        else:
            self.turn_total += roll
            print(f"Turn total is now {self.turn_total}")

    def hold(self):
        player = self.get_current_player()
        player.score += self.turn_total
        print(f"{player.name} holds. Total score is now {player.score}")
        self.switch_player()

    def get_current_player(self):
        return self.players[self.current_player_index]

    def play_turn(self):
        player = self.get_current_player()
        print(f"\n{player.name}'s turn:")
        print(f"Total score: {player.score}")

        while True:
            decision = input(f"{player.name}, do you want to 'roll' (r) or 'hold' (h)? ").strip().lower()
            if decision == 'r':
                self.roll_die()
                if self.turn_total == 0:  # Switch happens if a 1 is rolled
                    break
            elif decision == 'h':
                self.hold()
                break
            else:
                print("Invalid input. Please enter 'r' to roll or 'h' to hold.")

    def check_winner(self):
        for player in self.players:
            if player.score >= self.winning_score:
                return player
        return None

    def start_game(self):
        print("Welcome to the Pig game!")
        while True:
            self.play_turn()
            winner = self.check_winner()
            if winner:
                print(f"Congratulations, {winner.name}! You have won the game with {winner.score} points!")
                break

# Start the game
if __name__ == "__main__":
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")
    game = PigGame(player1_name, player2_name)
    game.start_game()

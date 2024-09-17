
import random

def roll_die():
    """Simulate rolling a die."""
    return random.randint(1, 6)

def play_turn(player_name):
    """Simulate a  turn for a player."""
    turn_total = 0
    while True:
        roll = roll_die()
        print(f"{player_name} rullede: {roll}")
        if roll == 1:
            print(f"{player_name} mistede alle point for denne runde!\n")
            return 0
        else:
            turn_total += roll
            print(f"{player_name}'s foreløbige score for denne runde: {turn_total}")
            response = input("Vil du rulle igen? (y/n) ")
            if response.lower() != 'y':
                return turn_total

def pig_game(winning_score):
    """Main function to play the Pig game."""
    player_scores = {"Spiller 1": 0, "Spiller 2": 0}
    current_player = "Spiller 1"

    while True: #all(score < winning_score for score in player_scores.values()):
        print(f"\nDet er {current_player}'s tur.")
        round_score = play_turn(current_player)
        player_scores[current_player] += round_score
        print(f"{current_player}'s totale score: {player_scores[current_player]}")

        if player_scores[current_player] >= winning_score:
            print(f"\n{current_player} har vundet spillet med {player_scores[current_player]} point!")
            break

        # Switch to the other player
        current_player = "Spiller 1" if current_player == "Spiller 2" else "Spiller 2"

if __name__ == "__main__":
    pig_game(100)

import random

def rollDie():
    return random.randint(1,6)

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
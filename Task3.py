import secrets
import time

class RockPaperScissorsGame:
    """A professional terminal-based Rock-Paper-Scissors game with score tracking."""
    
    def __init__(self):
        # Using a list for indexing and clean validation
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0

    def get_computer_choice(self) -> str:
        """Securely selects a random move for the computer."""
        return secrets.choice(self.choices)

    def determine_winner(self, user: str, computer: str) -> str:
        """Evaluates the round and updates scores. Returns result string."""
        if user == computer:
            self.ties += 1
            return "It's a tie!"
            
        # Define winning conditions where key beats value
        winning_rules = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        
        if winning_rules[user] == computer:
            self.user_score += 1
            return "🎉 You win this round!"
        else:
            self.computer_score += 1
            return "💻 Computer wins this round!"

    def display_scoreboard(self):
        """Prints a clean summary of current standings."""
        print("\n" + "="*30)
        print("          SCOREBOARD          ")
        print("="*30)
        print(f" Player Score   : {self.user_score}")
        print(f" Computer Score : {self.computer_score}")
        print(f" Total Ties     : {self.ties}")
        print("="*30 + "\n")


def main():
    print("=========================================")
    print("     ROCK, PAPER, SCISSORS ARENA        ")
    print("=========================================")
    
    game = RockPaperScissorsGame()
    
    while True:
        print("\nAvailable moves: Rock, Paper, Scissors")
        user_input = input("Enter your choice (or type 'quit' to exit): ").strip().lower()
        
        if user_input == 'quit':
            print("\nThanks for playing!")
            game.display_scoreboard()
            break
            
        if user_input not in game.choices:
            print("❌ Invalid input! Please check your spelling and try again.")
            continue
            
        # Computer choice with a slight delay effect for "suspense"
        print("\nComputer is choosing...")
        time.sleep(0.6)
        computer_choice = game.get_computer_choice()
        
        # Display Selections
        print(f"\n👉 Your Choice     : {user_input.capitalize()}")
        print(f"👉 Computer Choice : {computer_choice.capitalize()}")
        
        # Determine and show round outcome
        result = game.determine_winner(user_input, computer_choice)
        print(f"\n✨ {result} ✨")
        
        # Print scoreboard
        game.display_scoreboard()
        
        # Ask to play again
        play_again = input("Do you want to play another round? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nFinal standings before you leave:")
            game.display_scoreboard()
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

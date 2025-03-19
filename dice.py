from random import randint

class Dice:
    def __init__(self):
        self.user_choice = None
        self.computer_choice = None
        self.attempts = 0

    def get_user_choice(self):
        while True:
            try:
                self.user_choice = int(input("Please enter your choice (1-6):"))
                if 1 <= self.user_choice <= 6:
                    break
                else:
                    print("Invalid choice,please enter a number between 1-6.")
            except ValueError:
                print("Invalid input,please enter a number.")

    def get_computer_choice(self):
        self.computer_choice = randint(1,6)

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return "You won!"

        else:
            return "You lost! try again."

    def play(self):
        print("Welcome to the Dice Game!")
        while True:
            self.attempts += 1
            self.get_user_choice()
            self.get_computer_choice()
            print(f"You chose: {self.user_choice}")
            print(f"Computer chose: {self.computer_choice}")
            result = self.determine_winner()
            print(result)
            if result == "You won!":
                break

if __name__ == "__main__":
    game = Dice()
    game.play()






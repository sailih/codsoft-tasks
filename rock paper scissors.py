import tkinter as tk
from random import choice

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("300x200")
        self.player_score = 0
        self.computer_score = 0

        self.player_score_label = tk.Label(self.window, text="Player Score: 0", font=("Arial", 12))
        self.player_score_label.pack()

        self.computer_score_label = tk.Label(self.window, text="Computer Score: 0", font=("Arial", 12))
        self.computer_score_label.pack()

        self.result_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.result_label.pack()

        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT)

        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT)

        self.scissors_button = tk.Button(self.window, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT)

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = choice(choices)

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = "Player wins!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label['text'] = f"Player: {player_choice}, Computer: {computer_choice}, {result}"
        self.player_score_label['text'] = f"Player Score: {self.player_score}"
        self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
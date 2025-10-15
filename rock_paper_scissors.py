# 🎨 Colorful Rock-Paper-Scissors GUI
# Codsoft Python Internship - Task 3

import tkinter as tk
from tkinter import messagebox
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win! 🎉"
        user_score += 1
    else:
        result = "Computer wins! 💻"
        computer_score += 1
    
    user_choice_label.config(text=f"Your Choice: {user_choice}", fg="blue")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}", fg="red")
    result_label.config(text=result, fg="green" if "win" in result else "orange" if "tie" in result else "red")
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}", fg="purple")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your Choice: ", fg="black")
    computer_choice_label.config(text="Computer Choice: ", fg="black")
    result_label.config(text="Result: ", fg="black")
    score_label.config(text="Score -> You: 0 | Computer: 0", fg="black")

root = tk.Tk()
root.title("🕹️ Rock-Paper-Scissors Game")
root.geometry("450x400")
root.config(bg="#F0F8FF") 
root.resizable(False, False)

tk.Label(root, text="🕹️ Rock-Paper-Scissors", font=("Comic Sans MS", 18, "bold"), bg="#F0F8FF", fg="#FF4500").pack(pady=10)

user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12, "bold"), bg="#F0F8FF")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 12, "bold"), bg="#F0F8FF")
computer_choice_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#F0F8FF")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score -> You: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="#F0F8FF")
score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#F0F8FF")
button_frame.pack(pady=20)

button_colors = {"Rock": "#FF6347", "Paper": "#3CB371", "Scissors": "#1E90FF"}

for choice in choices:
    tk.Button(button_frame, text=choice, width=10, font=("Arial", 12, "bold"),
              bg=button_colors[choice], fg="white",
              command=lambda c=choice: play(c)).pack(side="left", padx=10)

tk.Button(root, text="Reset Game", width=15, font=("Arial", 12, "bold"), bg="#FFD700", fg="black", command=reset_game).pack(pady=10)

root.mainloop()

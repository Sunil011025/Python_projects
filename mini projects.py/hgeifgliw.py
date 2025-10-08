import tkinter as tk
from tkinter import messagebox
import random
import hangman_stages
import word_file

# Game setup
lives = 5
chosen_word = random.choice(word_file.words)
display = ['_'] * len(chosen_word)

# Functions
def update_display():
    word_label.config(text=' '.join(display))
    stage_label.config(text=hangman_stages.stages[lives])

def guess_letter():
    global lives, chosen_word
    guessed_letter = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)  # Clear the entry field

    if not guessed_letter or len(guessed_letter) != 1:
        messagebox.showwarning("Invalid Input", "Please enter a single letter!")
        return

    if guessed_letter in display or guessed_letter not in 'abcdefghijklmnopqrstuvwxyz':
        messagebox.showwarning("Invalid Input", "Letter already guessed or invalid character!")
        return

    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guessed_letter:
                display[position] = guessed_letter
    else:
        global lives
        lives -= 1

    update_display()
    check_game_over()

def check_game_over():
    global lives, chosen_word
    if '_' not in display:
        messagebox.showinfo("Congrats", "You win!")
        reset_game()
    elif lives == 0:
        messagebox.showinfo("Game Over", f"You lose! The word was '{chosen_word}'.")
        reset_game()

def reset_game():
    global lives, chosen_word, display
    lives = 5
    chosen_word = random.choice(word_file.words)
    display = ['_'] * len(chosen_word)
    update_display()

# GUI Setup
root = tk.Tk()
root.title("Hangman Game")

# Display the word
word_label = tk.Label(root, text=' '.join(display), font=("Helvetica", 18))
word_label.pack(pady=10)

# Display the hangman stage
stage_label = tk.Label(root, text=hangman_stages.stages[lives], font=("Courier", 12), justify="left")
stage_label.pack(pady=10)

# Entry and buttons
guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Helvetica", 14))
guess_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Helvetica", 14))
reset_button.pack(pady=5)

# Start the GUI loop
update_display()
root.mainloop()

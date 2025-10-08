import random
import tkinter as tk
from tkinter import messagebox
import hangman_stages
import word_file

# Initialize game variables
lives = 6
chosen_word = random.choice(word_file.words)
display = ['_'] * len(chosen_word)
guessed_letters = set()

def update_display():
    """Update the displayed word on the GUI."""
    word_label.config(text=' '.join(display))

def guess_letter():
    """Handle the logic when the player guesses a letter."""
    global lives
    guessed_letter = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)

    if len(guessed_letter) != 1 or not guessed_letter.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if guessed_letter in display or guessed_letter in guessed_letters:
        messagebox.showinfo("Already Guessed", f"You already guessed '{guessed_letter}'.")
        return

    guessed_letters.add(guessed_letter)
    
    # Check guessed letter
    correct_guess = False
    for position in range(len(chosen_word)):
        if chosen_word[position] == guessed_letter:
            display[position] = guessed_letter
            correct_guess = True

    if not correct_guess:
        lives -= 1
        hangman_label.config(text=hangman_stages.stages[lives])

    # Update the display
    update_display()

    # Check for game end
    if '_' not in display:
        messagebox.showinfo("HANGMAN GAME", "You win!!")
        reset_game()
    elif lives == 0:
        messagebox.showinfo("HANGMAN GAME", f"You lose!! The word was: {chosen_word}")
        reset_game()

    letter_entry.focus()  # keep focus for smooth input

def reset_game():
    """Reset the game state to play again."""
    global lives, chosen_word, display, guessed_letters
    lives = 6
    chosen_word = random.choice(word_file.words)
    display = ['_'] * len(chosen_word)
    guessed_letters = set()
    hangman_label.config(text=hangman_stages.stages[lives])
    update_display()
    letter_entry.focus()

# Create the main Tkinter window
window = tk.Tk()
window.title("HANGMAN GAME")

# Word display
word_label = tk.Label(window, text=' '.join(display), font=("Helvetica", 18))
word_label.pack(pady=20)

# Hangman stage display (start with full lives)
hangman_label = tk.Label(window, text=hangman_stages.stages[lives], font=("Courier", 12))
hangman_label.pack(pady=20)

# Letter entry
letter_entry = tk.Entry(window, font=("Helvetica", 14))
letter_entry.pack(pady=10)
letter_entry.focus()

# Guess button
guess_button = tk.Button(window, text="Guess", command=guess_letter, font=("Helvetica", 14))
guess_button.pack(pady=10)

# Reset button
reset_button = tk.Button(window, text="Reset Game", command=reset_game, font=("Helvetica", 14))
reset_button.pack(pady=10)

# Start the game loop
update_display()
window.mainloop()

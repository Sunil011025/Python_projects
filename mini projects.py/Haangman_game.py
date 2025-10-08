import random
import hangman_stages
import word_file
lives = 5
chosen_word = random.choice(word_file.words)
# print(chosen_word)  # Uncomment this line if you want to debug and see the chosen word

display = ['_'] * len(chosen_word)  # Simplified initialization
print(' '.join(display))  # Show underscores with spaces

game_over = False
while not game_over:
    guessed_letter = input("\nGuess a letter: ").lower()
    print()

    # Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(' '.join(display))  # Display the current state of the word with spaces

    # Deduct a life for incorrect guesses
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("\nYou lose!!")
    
    # Check if the player has won
    if '_' not in display:
        game_over = True
        print("\nYou win!!")
    
    # Print the current hangman stage
    print(hangman_stages.stages[lives])

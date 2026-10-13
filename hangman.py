import random

random_words = ['apple', 'carrot', 'orange', 'coconut', 'lemon']
secret_word = random.choice(random_words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

while wrong_guesses < max_wrong:
    # Show the hidden word
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display)

    # Check if player won
    if "_" not in display:
        print("You win! The word was:", secret_word)
        break

    # Ask for a guess
    guess = input("Guess a letter: ").lower()

    # Validate guess
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess and check
    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print(f"Wrong! You have {max_wrong - wrong_guesses} guesses left.")

else:
    print("You lose! The word was:", secret_word)